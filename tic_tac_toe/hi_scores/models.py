from django.db import models

class Score(models.Model):
	class Meta:
		verbose_name = ('Score')
		verbose_name_plural = ('Scores')

	initials = models.CharField(max_length=3)
	score = models.PositiveIntegerField()

	def __unicode__(self):
		return "%s %s" % (self.initials, self.score)
	