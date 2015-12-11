{% extends "base.html" %}

{% block content %}

Your time was <?php echo $_GET["minutes"]; ?> minutes<br>
and <?php echo $_GET["seconds"]; ?> seconds<br>
This is <?php total_seconds = (minutes * 60) + seconds; ?> seconds total<br>

{% endblock %}