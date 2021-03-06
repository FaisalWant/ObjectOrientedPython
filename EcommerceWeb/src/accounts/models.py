from django.db import models
from django.contrib.auth.models import(
	AbstractBaseUser,
	BaseUserManager
	)
class UserManager(BaseUserManager):
	def create_user(self, email, full_name, password=None, is_active=True,is_staff= False, is_admin=False
		):
		if not email:
			raise ValueError("user must have an email address")
		if not password:
			raise ValueError("user must have password")
		if not full_name:
			raise ValueError("user must have fullname")

		user_obj = self.model(
			email= self.normalize_email(email),
			full_name= full_name)

		user_obj.set_password(password)
		user_obj.staff=is_staff
		user_obj.admin=is_admin
		user_obj.active= is_active
		user_obj.save(using=self._db)
		return user_obj
	

	def create_staffuser(self, email, full_name, password=None):
		user= self.create_user(
			email, 
			full_name, 
			password=password,
			is_staff=True)
		return user
	
	def create_superuser(self, email,full_name, password=None):
		user= self.create_user(
			email, 
			full_name,
			password=password,
			is_staff=True,
			is_admin=True
			)
		return user	


# Create your models here.
class User(AbstractBaseUser):
	email = models.EmailField(unique=True, max_length=255)
	full_name= models.CharField(max_length=255, blank=True, null=True)
	active = models.BooleanField(default=True)
	staff = models.BooleanField(default=False)
	admin = models.BooleanField(default=False)
	timestamp= models.DateTimeField(auto_now_add=True)
	USERNAME_FIELD= 'email'
	REQUIRED_FIELDS =['full_name']

	objects = UserManager()
	def get_full_name(Self):
		return self.email


	def get_short_name(self):
		return self.email


	def __str__(self):
		return self.email


	def has_perm(self, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True


	@property
	def is_staff(self):
		return self.staff


	@property
	def is_admin(self):
		return self.staff

	@property
	def is_admin(self):
		return self.admin








class GuestEmail(models.Model):
	email=models.EmailField()
	active= models.BooleanField(default=True)
	update= models.DateTimeField(auto_now= True)
	timestamp= models.DateTimeField(auto_now_add=True)
	def __str__ (self):
		return self.email 