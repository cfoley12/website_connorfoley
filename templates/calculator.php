{% extends "base.html" %}

{% block content %}

<?php
$minutes = $_GET("minutes");
$seconds = $_GET("seconds");
$total_seconds = ($minutes * 60) + $seconds;
?>

Your time was <?php echo $minutes; ?> minutes<br>
and <?php echo $seconds; ?> seconds<br>
This is <?php echo $total_seconds; ?> seconds total<br>

{% endblock %}