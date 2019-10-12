from uuid import uuid4

from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin


class UserManager(BaseUserManager):
    """Manager for User model"""
    def create_user(self, email, password, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError("User must have an email address")

        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.twix_groups.add(Group.objects.create(
            name='Personal', users=user, admins=user
        ))

        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and save a superuser in the system"""
        user = self.create(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User model"""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        app_label = 'user'
        default_related_name = 'users'

    def __str__(self):
        return self.email


class Board(models.Model):
    """Board model"""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    is_personal = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)

    class Meta:
        app_label = 'twix'
        default_related_name = 'boards'

    def __str__(self):
        return self.name


class Task(models.Model):
    """Task model"""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    is_done = models.BooleanField()
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    class Meta:
        app_label = 'twix'
        default_related_name = 'tasks'

    def __str__(self):
        return self.name


class Group(models.Model):
    """Group model"""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    admins = models.ManyToManyField(User, related_name='admins')
    users = models.ManyToManyField(User)

    class Meta:
        app_label = 'twix'
        default_related_name = 'twix_groups'

    def __str__(self):
        return self.name
