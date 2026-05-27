from flask import Flask, render_template, request, flash, redirect, url_for, Response
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "chaba-massage-dev-key")

# Business data
BUSINESS = {
    "name": "Thai Massage In Hove",
    "phone": "07873 969610",
    "phone_link": "tel:+447873 969610",
    "whatsapp": "https://wa.me/447873969610",
    "email": "jojocollins@gmail.com",
    "email_link": "Church Road,mailto:jojocollins@gmail.com?subject=Appointment%20Booking%20-%20Thai%Massage%20In%20Hove",
    "address": "96-98 Church Rd, Brighton and Hove, Hove BN3 2EB",
    "address_full": "96-98 Church Rd, Brighton and Hove, Hove BN3 2EB",
    "google_maps_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d9135.680115138497!2d-0.1905468106270145!3d50.82768862390706!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x487585388e368f39%3A0x14325fee8ce3d1f4!2sThai%20Massage%20in%20hove!5e1!3m2!1sen!2suk!4v1779919999092!5m2!1sen!2suk",
    "google_maps_link": "https://maps.app.goo.gl/WiwSh1aoDrXYf4AU7",
    "facebook": "#",
    "rating": "5.0",
    "reviews_count": "70",
    "hours": {
        "Monday": "10:00 AM – 10:00 PM",
        "Tuesday": "10:00 AM – 10:00 PM",
        "Wednesday": "10:00 AM – 10:00 PM",
        "Thursday": "10:00 AM – 10:00 PM",
        "Friday": "10:00 AM – 8:00 PM",
        "Saturday": "10:00 AM – 8:00 PM",
        "Sunday": "Closed",
    },
}

SERVICES = [
    {
        "name": "Full Body Oils Massage",
        "description": "A deeply relaxing full body massage using warm aromatic oils to ease tension, improve circulation, and leave your skin feeling nourished and revitalised.",
        "icon": "oils",
    },
    {
        "name": "Traditional Thai Massage",
        "description": "An ancient healing art combining acupressure, stretching, and energy work. Performed fully clothed, this full body treatment restores flexibility and balance.",
        "icon": "thai",
    },
    {
        "name": "Back, Neck & Shoulder",
        "description": "Targeted therapy focusing on the areas where tension builds most. Ideal for office workers and those suffering from stress-related pain.",
        "icon": "back",
    },
    {
        "name": "Foot, Hand Massage & Reflexology",
        "description": "Pressure point therapy on the feet and hands to stimulate the body's natural healing processes and promote deep relaxation throughout.",
        "icon": "foot",
    },
    {
        "name": "Head & Shoulders",
        "description": "A soothing treatment to relieve headaches, reduce stress, and release tension held in the scalp, neck, and shoulder muscles.",
        "icon": "head",
    },
    {
        "name": "Head & Face Massage",
        "description": "A gentle, calming massage of the head and face that relieves sinus pressure, eases headaches, and promotes a sense of deep calm.",
        "icon": "face",
    },
    {
        "name": "Deep / Soft Tissue",
        "description": "Firm pressure techniques targeting deeper muscle layers to break down knots, relieve chronic pain, and restore full range of movement.",
        "icon": "deep",
    },
]

PRICING = [
    {"duration": "30 minutes", "price": "£35"},
    {"duration": "60 minutes", "price": "£60"},
    {"duration": "90 minutes", "price": "£85"},
    {"duration": "120 minutes", "price": "£110"},
]

TESTIMONIALS = [
    {
        "text": "Lovely environment, professional, friendly, traditional and knowledgeable therapist. I left feeling completely renewed.",
        "author": "Google Review",
        "stars": 5,
    },
    {
        "text": "I came in with terrible back pain and left completely free of it. Thai Massage In Hove has magic hands. Highly recommend!",
        "author": "Google Review",
        "stars": 5,
    },
    {
        "text": "Excellent deep tissue massage that really helped with my cervical and lumbar spine pain. Same-day availability was a bonus!",
        "author": "Google Review",
        "stars": 5,
    },
]


@app.route("/")
def home():
    return render_template(
        "index.html",
        business=BUSINESS,
        services=SERVICES[:3],
        pricing=PRICING,
        testimonials=TESTIMONIALS,
    )


@app.route("/about")
def about():
    return render_template("about.html", business=BUSINESS)


@app.route("/services")
def services():
    return render_template(
        "services.html", business=BUSINESS, services=SERVICES, pricing=PRICING
    )


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        service = request.form.get("service")
        message = request.form.get("message")

        if name and email and message:
            flash("Thank you for your message! We will get back to you soon.", "success")
        else:
            flash("Please fill in all required fields.", "error")

        return redirect(url_for("contact"))

    return render_template(
        "contact.html", business=BUSINESS, services=SERVICES
    )


@app.route("/gift-vouchers")
def gift_vouchers():
    return render_template(
        "gift-vouchers.html", business=BUSINESS, pricing=PRICING
    )


@app.route("/robots.txt")
def robots():
    txt = "User-agent: *\nAllow: /\n\nSitemap: https://thaimassageinhove.com/sitemap.xml\n"
    return Response(txt, mimetype="text/plain")

@app.route("/sitemap.xml")
def sitemap():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://thaimassageinhove.com/</loc><priority>1.0</priority></url>
  <url><loc>https://thaimassageinhove.com/about</loc><priority>0.8</priority></url>
  <url><loc>https://thaimassageinhove.com/services</loc><priority>0.9</priority></url>
  <url><loc>https://thaimassageinhove.com/gift-vouchers</loc><priority>0.7</priority></url>
  <url><loc>https://thaimassageinhove.com/contact</loc><priority>0.9</priority></url>
</urlset>"""
    return Response(xml, mimetype="application/xml")
if __name__ == "__main__":
    app.run(debug=True, port=5001)
