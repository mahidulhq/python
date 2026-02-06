# COVID-19 Bangladesh Daily Notification

Fetches daily COVID-19 stats for Bangladesh and sends desktop notifications.

## Python Libraries Used

- `requests` - HTTP requests to Disease.sh API
- `plyer` - Cross-platform desktop notifications
- `time` - Sleep delays
- `schedule` - Optional scheduled execution (commented)

## API Used

**Disease.sh COVID-19 API**  
Endpoint: `https://disease.sh/v3/covid-19/countries/bangladesh`  
Returns JSON with `cases`, `deaths`, `recovered` fields.

## Features

- Daily notifications with formatted case numbers
- Two execution modes:
  1. **Simple loop**: Runs every 24 hours (`time.sleep(86400)`)
  2. **Scheduled**: Daily at 09:00 (commented code)

## Usage

```bash
pip install requests plyer schedule
python covidNotifier.py
```

## Code Flow

1. Fetches Bangladesh COVID data from Disease.sh API
2. Formats cases/deaths/recovered with commas
3. Sends desktop notification (10-second timeout)
4. Sleeps 24 hours, repeats indefinitely

## Notification Example

```
Title: COVID Bangladesh
Message: Cases: 2,045,678 Deaths: 29,123 Recovered: 1,987,654
```

***