from jinja2 import Template

persons = [
    {'name': 'Вадим', 'old': 18, 'weight': 91},
    {'name': 'Олег', 'old': 33, 'weight': 78},
    {'name': 'Егор', 'old': 51, 'weight': 66},
    {'name': 'Василий', 'old': 18, 'weight': 86},
    {'name': 'Анатолий', 'old': 22, 'weight': 99},
]

html = """
{% macro list_users(list_of_users) -%}
<ul>
{% for u in list_of_users -%}
    <li>{{ u.name }} {{ caller(u)}}
{% endfor -%}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
        <li>age: {{user.age}}
        <li>weight: {{ user.weight }}
    </ul>
{%- endcall -%}
"""

tm = Template(html)
msg = tm.render(users=persons)
print(msg)