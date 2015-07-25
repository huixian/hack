from django.contrib import admin
from .models import NodeType
from .models import Node
from .models import Reading

# Register your models here.

admin.site.register(NodeType)
admin.site.register(Node)
admin.site.register(Reading)

class NodeAdmin(admin.ModelAdmin):
    list_display = ('node_id', 'node_type', 'node_name')