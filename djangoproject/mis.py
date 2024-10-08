

{% extends 'base.html' %}
{% load static %}

{% block extra_css %}
<style>
    .video-background {
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        width: auto;
        height: auto;
        z-index: -1000;
        background-size: cover;
    }
    .content-overlay {
        position: relative;
        z-index: 1;
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 10px;
    }
</style>
{% endblock %}

{% block content %}
<video autoplay muted loop class="video-background">
    <source src="{% static 'video/video.mp4' %}" type="video/mp4">
    Your browser does not support the video tag.
</video>

<div class="container mt-5">
    <div class="content-overlay">
        <h2>{{ user.username }}'s Profile</h2>
        <div class="card">
            <div class="card-body">
                <div class="row">
                    <div class="col-md-4">
                        {% if customer_profile.profile_picture %}
                            <img src="{{ customer_profile.profile_picture.url }}" alt="Profile Picture" class="img-fluid rounded-circle mb-3" style="max-width: 200px;">
                        {% else %}
                            <img src="{% static 'images/default_profile_pic.png' %}" alt="Default Profile Picture" class="img-fluid rounded-circle mb-3" style="max-width: 200px;">
                        {% endif %}
                    </div>
                    <div class="col-md-8">
                        <p><strong>Username:</strong> {{ user.username }}</p>
                        <p><strong>Email:</strong> {{ user.email }}</p>
                        {% if customer_profile %}
                            <p><strong>Name:</strong> {{ customer_profile.name }}</p>
                            <p><strong>Address:</strong> {{ customer_profile.address|default:"Not provided" }}</p>
                            <p><strong>Phone:</strong> {{ customer_profile.phone|default:"Not provided" }}</p>
                        {% else %}
                            <p><strong>Address:</strong> Not provided</p>
                            <p><strong>Phone:</strong> Not provided</p>
                        {% endif %}
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

{% if user.is_authenticated %}
    <div class="container mt-3">
        <a href="{% url 'edit_profile' %}" class="btn btn-primary">Edit Profile</a>
    </div>
{% endif %}
{% endblock %}