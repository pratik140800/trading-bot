import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email_alert(results_df):
    """Sends an email with the Screener results."""
    
    # Convert results to a clean HTML table
    html_table = results_df.to_html(index=False, border=1, justify='center')
    
    message = Mail(
        from_email='your_email@gmail.com',  # Must be verified in SendGrid
        to_emails='your_trading_email@gmail.com',  # Where you want alerts
        subject=f'🚀 Daily Trading Signals - {datetime.now().strftime("%Y-%m-%d")}',
        html_content=f"""
        <h2>Market Signals for Today</h2>
        <p>Here are the trades to take based on your strategy:</p>
        {html_table}
        <br>
        <p><b>Action Plan:</b><br>
        - <span style="color:green">BUY 🟢</span>: Enter Long position.<br>
        - <span style="color:red">SELL 🔴</span>: Enter Short position.<br>
        - <span style="color:orange">EXIT ⚠️</span>: Close existing position.<br>
        - <span style="color:gray">HOLD ➖</span>: No action needed.</p>
        """
    )
    
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(f"✅ Email sent! Status Code: {response.status_code}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")