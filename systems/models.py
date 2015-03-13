 from django.db import models
import os


class Media(models.Model):
	"""
	Is there a reusable media app that can handle our media?
	We want users to be able to use the media class to store 
	media like videos, attachments, images, etc
	"""
	video_url = models.URLField()
	image_file = models.ImageField(upload_to=os.path.dirname(os.path.dirname(__file__)))


class Drawing(models.Model):
	"""
	Is there a drawing app we can import???
	"""

class Thermal_Properties(models.Model):
	"""
	The Thermal Properties class ...
	"""
	heat_capacity = models.CharField(max_length=100)
	expansion = models.CharField(max_length=100)
	conductivity = models.CharField(max_length=100)
	stress = models.CharField(max_length=100)


class Chemical_Properties(models.Model):
	"""
	The Chemical Properties class ...
	"""
	#flamability = this should be a MSDS number?
	heat_of_combustion = models.CharField(max_length=100)
	toxicity = models.CharField(max_length=100)
	ability_to_oxidize = models.CharField(max_length=100)
	radioactivity = models.CharField(max_length=100)
	chemical_stability = models.CharField(max_length=100)
	half_life = models.CharField(max_length=100)
	boiling_point = models.CharField(max_length=100)
	specific_gravity = models.CharField(max_length=100)
	vapor_pressure = models.CharField(max_length=100)
	vapor_density = models.CharField(max_length=100)
	soluability_in_water = models.CharField(max_length=100)

class Physical_Properties(models.Model):
	"""
	The Physical_Properties
	"""
	color = models.CharField(max_length=200)
	odor = models.CharField(max_length=200)

class Magnetic_Properties(models.Model):
	"""
	The Magnetic Properties class ...
	"""
	gauss = models.CharField(max_length=200)

class Acoustic_Properties(models.Model):
	"""
	The Acoustic Properties class ...
	"""
	vibrational_modes = models.CharField(max_length=200)


class Material(models.Model):
	"""
	The Material class ...
	"""
	common_name = models.CharField(max_length=100)
	scientific_name = models.CharField(max_length=100)
	thermal_properties = models.ForeignKey(Thermal_Properties)
	chemical_properties = models.ForeignKey(Chemical_Properties)
	magnetic_properties = models.ForeignKey(Magnetic_Properties)
	acoustic_properties = models.ForeignKey(Acoustic_Properties)
	physical_properties = models.ForeignKey(Physical_Properties)

	#Everything is stored in metric units (converted in front end if needed
	mass = models.CharField(max_length=100)
	volume = models.CharField(max_length=100)


class Resource(models.Model):
	"""
	The Resource class ...
	"""
	materials = models.ForeignKey(Material)
	#energy = models.DecimalField()
	services = models.TextField()
	knowledge = models.TextField()
	other = models.TextField()


'''
class Component(models.Model):
	"""
	The Component class ...
	"""
	name = models.CharField(max_length=200)
	#life_time = models.DateTimeField()
	#drawing = models.ManyToMany(Drawing)
	weight = models.DecimalField()
	#resources = models.ManyToManyField(Media)
	subcomponent = models.ManyToManyField(Component)
	materials = models.ManyToManyField(Resource)


class Category(models.Model):
	"""
	The Category class ..
	"""
	name = models.CharField(max_length=20)


class Step(models.Model):
	"""
	The Step class ...
	"""
	title = models.CharField(max_length=200)
	subtitle = models.CharField(max_length=200)
	category = models.CharField(choices=(CATEGORY_CHOICES))
	number = models.PositiveIntegerField()
	#Each step belongs to a direction
	directions = models.

	#media = models.ManyToManyField(Media) #Media includes additional attahcments, videos, etc
	max_time_estimate = models.TimeField()
	min_time_estimate = models.TimeField()
	resources = models.ManyToManyField(Resource)


class Directions(models.Model):
	#Each direction has many steps
	step = models.ForeignKey(Step)


class System(models.Model):
	"""
	The System class ...
	"""
	title = models.CharField(max_length=200) #title of the system
	description = models.TextField() #brief description of the system
	subsystem = models.ManyToManyField(System)
	category = models.ManyToManyField(Category)
	purpose = models.CharField(max_length=500)
	supporting_media = models.ManyToManyField(Media)
	components = models.ManyToManyField(Component)

	#Directions for assembly, maintenance and disassembly
	directions = models.ForeignKey(Directions)

	def __unicode__(self):
		return self.title
'''