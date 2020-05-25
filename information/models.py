from django.db import models
from django.db.models import CharField





class Common(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(null=True, unique=True, blank=True)
    section = models.TextField(null=True)
    template_name: CharField = models.CharField(max_length=30, null=True, )
    hreflogo = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=300, blank=True)
    descrtionmeta = models.TextField(max_length=300, blank=True)
    keywordsmeta = models.TextField(max_length=300, blank=True)

    class Meta:
        abstract = True

class Navconstruct(Common):

    def __str__(self):
        return self.name

class Subnavigator(Common):
    subname = models.ForeignKey('Navconstruct', on_delete=models.CASCADE, related_name="sub", null=True, blank=True)
    projname = models.ForeignKey('Footercont', on_delete=models.CASCADE, related_name="project", null=True, blank=True)
    def __str__(self):
        return self.name

class Subsubnav(Common):
    subname = models.ForeignKey('Subnavigator', on_delete=models.CASCADE, related_name="sub", null=True)
    def __str__(self):
        return self.name

class Social(models.Model):
    title = models.CharField(max_length=30)
    href = models.URLField(null=True)
    classname = models.CharField(max_length=30)
    text = models.TextField(blank=True)
    social = models.BooleanField()
    def __str__(self):
        return self.title

class Footercont(models.Model):

    title = models.CharField(max_length=30)
    classname = models.CharField(max_length=100)
    classdiv= models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

class Footer(models.Model):
    type = models.ForeignKey('Footercont', on_delete=models.CASCADE, related_name="type", null=True)
    title = models.CharField(max_length=30)
    hreflogo = models.CharField(max_length=100, blank=True)
    classul = models.CharField(max_length=100, blank=True)
    classdir = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

class Text(models.Model):
    subname = models.ForeignKey('Footer', on_delete=models.CASCADE, related_name="textsub", null=True)
    title = models.CharField(max_length=30, blank=True)
    footertext = models.TextField(blank=True)
    def __str__(self):
        return self.title

class Page(models.Model):
    subname = models.ForeignKey('Navconstruct', on_delete=models.CASCADE, related_name="text", null=True)
    projname = models.ForeignKey('Subnavigator', on_delete=models.CASCADE, related_name="subtext", null=True, blank=True)
    title = models.CharField(max_length=30, blank=True)
    textup = models.TextField(blank=True)
    quote = models.TextField(blank=True)
    textdown = models.TextField(blank=True)
    def __str__(self):
        return self.title

class Slider(models.Model):
    projname = models.ForeignKey('Subnavigator', on_delete=models.CASCADE, related_name="subslider", null=True, blank=True)
    name = models.CharField(max_length=30)
    hreflogo = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name



class Projects(models.Model):
    subname = models.ForeignKey('Navconstruct', on_delete=models.CASCADE, related_name="proj", null=True)
    projname = models.ForeignKey('Subnavigator', on_delete=models.CASCADE, related_name="subproj", null=True, blank=True)
    title = models.CharField(max_length=100, blank=True)
    href = models.CharField(max_length=100, blank=True)
    dafilter = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

class Example(models.Model):
    example = models.ForeignKey('Projects', on_delete=models.CASCADE, related_name="example", null=True)
    title = models.CharField(max_length=100, blank=True)
    href = models.CharField(max_length=200, blank=True)
    src = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(null=True, unique=True, blank=True)
    projectname = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=300, blank=True)
    keywords = models.TextField(max_length=300, blank=True)



    def __str__(self):
        return self.projectname

class Pictures(models.Model):
    name = models.ForeignKey('Example', on_delete=models.CASCADE, related_name="pictures", null=True)
    href1 = models.CharField(max_length=200, blank=True)
    href2 = models.CharField(max_length=100, blank=True)
    href3 = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.name.projectname

class Short(models.Model):
    name = models.ForeignKey('Example', on_delete=models.CASCADE, related_name="short", null=True)
    predescription = models.TextField(blank=True)
    namecategory = models.CharField(max_length=30)
    caregory = models.CharField(max_length=100)
    namefokus = models.CharField(max_length=30)
    fokus = models.CharField(max_length=100)
    namesite = models.CharField(max_length=30)
    site = models.CharField(max_length=100)
    nameduration = models.CharField(max_length=30)
    duration = models.CharField(max_length=100)
    def __str__(self):
        return self.name.projectname

class CommonInfo(models.Model):
    urlvideo = models.URLField(max_length=100, blank=True)
    blockquote = models.TextField(blank=True)
    paragraph = models.TextField(blank=True)
    titlenext = models.CharField(max_length=30, blank=True)
    textnext = models.TextField(blank=True)
    titlecoloumn = models.CharField(max_length=100, blank=True)
    titleparagraph = models.CharField(max_length=100, blank=True)

    class Meta:
        abstract = True

class Pagenext(CommonInfo):
    subname = models.ForeignKey('Navconstruct', on_delete=models.CASCADE, related_name="next", null=True)
    projname = models.ForeignKey('Subnavigator', on_delete=models.CASCADE, related_name="subnext", null=True, blank=True)
    title = models.CharField(max_length=100, blank=True)
    urljpg = models.CharField(max_length=100, blank=True)
    textup = models.TextField(blank=True)
    quote = models.TextField(blank=True)
    textdown = models.TextField(blank=True)
    def __str__(self):
        return self.title

class Pageproject(CommonInfo):
    name = models.ForeignKey('Example', on_delete=models.CASCADE, related_name="pageproject", null=True)
    def __str__(self):
        return self.name.projectname

class Faqblock (models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Faq (models.Model):
    name = models.ForeignKey('Faqblock',on_delete=models.CASCADE, related_name="faq", null=True)
    question = models.CharField(max_length=200)
    answer = models.TextField(blank=True)
    def __str__(self):
        return self.question

class Commoncontact(models.Model):
    name = models.CharField(max_length=50)
    answer = models.TextField(blank=True)
    class Meta:
        abstract = True

class Contact (Commoncontact):

    icon = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.name

class Etapy(Commoncontact):
    namenext = models.CharField(max_length=50, blank=True)
    answernext = models.TextField(blank=True)
    href = models.CharField(max_length=200, blank=True)
    href1 = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.name

class Contdecr (models.Model):
    title1 = models.CharField(max_length=100, blank=True)
    title2 = models.CharField(max_length=100, blank=True)
    title3 = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title1

class Pictslider(models.Model):
    hreflogo = models.CharField(max_length=100)

    def __str__(self):
        return self.hreflogo

class Textslider(models.Model):
    picture = models.ForeignKey('Pictslider',on_delete=models.CASCADE, related_name="picture", null=True)
    textblock =models.TextField(blank=True)
    textbldown = models.TextField(blank=True)
    clas = models.CharField(max_length=20, blank=True)


    def __str__(self):
        return self.picture.hreflogo

class Mpage(models.Model):
    name = models.CharField(max_length=30, blank=True)
    title = models.CharField(max_length=100, blank=True)
    textblock =models.TextField(blank=True)
    title1 = models.CharField(max_length=100, blank=True)
    textblock1 = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Values (Commoncontact):
    icon = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.name


# Create your models here.
