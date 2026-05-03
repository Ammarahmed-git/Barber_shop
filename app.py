#Nai ki dukaan

from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'barbershop-secret-2024'

# In-memory bookings store (use a DB in production)
bookings = []

SERVICES = [
    {"id": 1, "name": "Classic Cut", "price": 35, "duration": "30 min", "desc": "Precision scissor cut with styling"},
    {"id": 2, "name": "Fade & Taper", "price": 45, "duration": "45 min", "desc": "Sharp fade with seamless blend"},
    {"id": 3, "name": "Hot Towel Shave", "price": 40, "duration": "40 min", "desc": "Traditional straight razor experience"},
    {"id": 4, "name": "Beard Sculpt", "price": 30, "duration": "30 min", "desc": "Defined shape & expert grooming"},
    {"id": 5, "name": "Royal Package", "price": 95, "duration": "90 min", "desc": "Cut + Shave + Beard + Styling"},
    {"id": 6, "name": "Hair Color", "price": 65, "duration": "60 min", "desc": "Premium coloring & highlights"},
]

BARBERS = [
    {"id": 1, "name": "Marcus Steel", "specialty": "Fades & Tapers", "exp": "12 Years", "emoji": "✂️"},
    {"id": 2, "name": "Diego Reyes", "specialty": "Classic Cuts", "exp": "8 Years", "emoji": "💈"},
    {"id": 3, "name": "Jax Thornton", "specialty": "Beard Artistry", "exp": "10 Years", "emoji": "🪒"},
]

TIME_SLOTS = ["9:00 AM", "9:30 AM", "10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM",
              "12:00 PM", "1:00 PM", "1:30 PM", "2:00 PM", "2:30 PM", "3:00 PM",
              "3:30 PM", "4:00 PM", "4:30 PM", "5:00 PM", "5:30 PM", "6:00 PM"]

@app.route('/')
def index():
    return render_template('index.html', services=SERVICES, barbers=BARBERS, time_slots=TIME_SLOTS)

@app.route('/api/book', methods=['POST'])
def book():
    data = request.json
    booking = {
        "id": len(bookings) + 1,
        "name": data.get('name'),
        "email": data.get('email'),
        "phone": data.get('phone'),
        "service": data.get('service'),
        "barber": data.get('barber'),
        "date": data.get('date'),
        "time": data.get('time'),
        "price": data.get('price'),
        "created_at": datetime.now().isoformat()
    }
    bookings.append(booking)
    return jsonify({"success": True, "booking_id": booking["id"], "message": "Booking confirmed!"})

@app.route('/api/payment/create-intent', methods=['POST'])
def create_payment_intent():
    data = request.json
    amount = data.get('amount', 0)
    # Demo mode - in production use: stripe.PaymentIntent.create(amount=amount*100, currency='usd')
    return jsonify({
        "success": True,
        "client_secret": "demo_pi_secret_" + str(amount),
        "amount": amount,
        "currency": "USD",
        "demo_mode": True
    })

@app.route('/api/payment/confirm', methods=['POST'])
def confirm_payment():
    data = request.json
    # Demo confirmation - integrate real Stripe in production
    return jsonify({
        "success": True,
        "payment_id": "demo_pay_" + datetime.now().strftime('%Y%m%d%H%M%S'),
        "status": "succeeded",
        "message": "Payment successful! See you soon."
    })

@app.route('/api/services')
def get_services():
    return jsonify(SERVICES)

@app.route('/api/bookings')
def get_bookings():
    return jsonify(bookings)

if __name__ == '__main__':
    app.run(debug=True, port=5000)