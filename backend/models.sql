# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdsAd(models.Model):
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    image = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ads_ad'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CartCart(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.OneToOneField('PersonPerson', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cart_cart'


class CartCartitem(models.Model):
    quantity = models.PositiveIntegerField()
    cart = models.ForeignKey(CartCart, models.DO_NOTHING)
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cart_cartitem'
        unique_together = (('cart', 'product'),)


class CommentComment(models.Model):
    text = models.TextField()
    image = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    user = models.ForeignKey('PersonPerson', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'comment_comment'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FavoritesFavorite(models.Model):
    created_at = models.DateTimeField()
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    user = models.ForeignKey('PersonPerson', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'favorites_favorite'
        unique_together = (('user', 'product'),)


class OrderOrder(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    subject = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    out_trade_no = models.CharField(unique=True, max_length=64)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    paid_at = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    user = models.ForeignKey('PersonPerson', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_order'


class OrderOrderitem(models.Model):
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING)
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_orderitem'


class PersonPerson(models.Model):
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField()
    email = models.CharField(unique=True, max_length=254, blank=True, null=True)
    avatar = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(unique=True, max_length=150)
    phone = models.CharField(unique=True, max_length=15, blank=True, null=True)
    updated_at = models.DateTimeField()
    address = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'person_person'


class PostCommentPostcomment(models.Model):
    text = models.TextField()
    image = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    post = models.ForeignKey('PostsPost', models.DO_NOTHING)
    user = models.ForeignKey(PersonPerson, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'post_comment_postcomment'


class PostsContent(models.Model):
    text = models.TextField()
    image = models.CharField(max_length=100, blank=True, null=True)
    video = models.CharField(max_length=100, blank=True, null=True)
    post = models.OneToOneField('PostsPost', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'posts_content'


class PostsPost(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey(PersonPerson, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'posts_post'


class PostsPostTags(models.Model):
    post = models.ForeignKey(PostsPost, models.DO_NOTHING)
    tag = models.ForeignKey('PostsTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'posts_post_tags'
        unique_together = (('post', 'tag'),)


class PostsTag(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'posts_tag'


class ProductsAnimal(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'products_animal'


class ProductsCategory(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'products_category'


class ProductsProduct(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    image = models.CharField(max_length=100, blank=True, null=True)
    favorite_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'products_product'


class ProductsProductAnimals(models.Model):
    product = models.ForeignKey(ProductsProduct, models.DO_NOTHING)
    animal = models.ForeignKey(ProductsAnimal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'products_product_animals'
        unique_together = (('product', 'animal'),)


class ProductsProductCategories(models.Model):
    product = models.ForeignKey(ProductsProduct, models.DO_NOTHING)
    category = models.ForeignKey(ProductsCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'products_product_categories'
        unique_together = (('product', 'category'),)


class TestapiProduct(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'testapi_product'
