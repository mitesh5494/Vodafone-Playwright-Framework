# Vodafone UK E2E Automation Framework

A Playwright-based end-to-end automation framework for testing Vodafone UK's e-commerce purchase journeys across multiple product lines.

## 📋 Overview

This framework automates the complete purchase flow for Vodafone UK products using the **Page Object Model (POM)** pattern with data-driven test configuration. Tests generate comprehensive Word reports with timestamped screenshots for each step.

### Supported Product Journeys

| Product | Test Cases | Journey Steps |
|---------|------------|---------------|
| **Broadband (FTTP)** | `test_fttp_tc_acq` | Postcode → Address → Plan → Addon → Setup → Basket → Checkout |
| **Broadband (FTTH)** | `test_ftth_tc_acq` | Postcode → Address → Plan → Addon → Setup → Basket → Checkout |
| **Broadband (SOGEA)** | `test_sogea_tc_acq` | Postcode → Address → Plan → Addon → Setup → Basket → Checkout |
| **Fixed Wireless (FWA)** | `test_fwa_tc_acq` | Postcode → Address → Plan → Basket → Checkout |
| **SIM Only** | `test_simo_tc_acq` | Plan → Basket → Checkout |
| **Handset (Pay Monthly)** | `test_handsetpaym_tc_acq` | Plan → Device Config → Airtime → Addon → Basket → Checkout |

---

## 🏗️ Project Structure

```
VodafoneProject/
├── Tests/                          # Main test suite (Page Object Pattern)
│   ├── test_broadband_framework.py  # FTTP, FTTH, SOGEA broadband tests
│   ├── test_fwa.py                  # Fixed Wireless Access tests
│   ├── test_handset.py              # Handset/pay-monthly contract tests
│   └── test_simo.py                 # SIM-only tests
├── pageobject/                     # Page Object Model classes
│   ├── base_page.py                # Base class with locator wrappers & helpers
│   ├── landing_page.py             # Cookie acceptance, postcode entry
│   ├── address_page.py             # Address selection
│   ├── plans_page.py               # Plan selection (all product types)
│   ├── basket_page.py              # Basket validation & expansion
│   ├── checkout_page.py            # Checkout flow (personal, address, payment)
│   ├── addon_page.py               # Add-on selection
│   ├── bbsetup_page.py             # Broadband setup (digital voice, telecare)
│   ├── device_variants_page.py     # Device config (color, capacity, contract)
│   ├── phoneplan_page.py           # Phone plan tenure selection
│   └── airtime_plans_page.py       # Airtime plan selection
├── utils/                          # Utility modules
│   ├── locator_loader.py           # Loads locators from JSON
│   ├── screenshot_manager.py       # Captures screenshots + Word reports
│   └── test_data_loader.py         # Loads test data from JSON
├── test_data/                      # Test configuration (data-driven)
│   ├── testdata.json               # Test cases: postcodes, plans, checkout data
│   └── locators.json               # CSS/XPath selectors per page
├── conftest.py                     # Pytest fixtures (browser, page, report, URLs)
├── requirements.txt                # Python dependencies
├── .github/workflows/              # CI/CD pipeline
└── reports/                        # Generated Word reports (auto-created)
```

---

## ⚙️ Installation

### Prerequisites
- Python 3.12+
- Git

### Setup

```bash
# Clone the repository
git clone <repository-url>
cd VodafoneProject

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# Windows (CMD):
.\.venv\Scripts\activate.bat
# Linux/Mac:
source .venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium
playwright install-deps  # Linux only
```

---

## 🚀 Running Tests

### Basic Commands

```bash
# Run all tests
pytest Tests/ -v

# Run specific test file
pytest Tests/test_broadband_framework.py -v

# Run specific test case
pytest Tests/test_broadband_framework.py::test_fttp_tc_acq -v

# Run with Firefox instead of Chrome
pytest Tests/ --browsername=firefox -v

# Run with headed mode (see browser)
pytest Tests/ -v --headed

# Run in parallel (requires pytest-xdist)
pytest Tests/ -n auto -v
```

### Test Configuration

Tests are configured via `test_data/testdata.json`. Each test case contains:
- Product type (`broadband`, `fwa`, `simo`, `handset`)
- Postcode and address details
- Plan selection criteria (speed, plan name, TV package)
- Checkout information (personal details, payment)

### Locators

Element locators are centralized in `test_data/locators.json` for easy maintenance when UI changes.

---

## 📊 Reports

The framework automatically generates **Microsoft Word reports** with:
- Test case name and execution timestamp
- Step-by-step screenshots with descriptive names
- Timestamps for each action
- Failure screenshots with error details

Reports are saved to: `reports/<test_case_name>/<test_case_name>.docx`

Screenshots are saved to: `reports/<test_case_name>/screenshots/`

---

## 🔧 Key Features

### Page Object Model
Clean separation of test logic from page interactions. Each page has a dedicated class with reusable methods.

### Data-Driven Testing
All test data externalized in JSON - no hardcoded values in test code.

### Centralized Locators
CSS/XPath selectors maintained in a single JSON file for easy updates.

### Automatic Reporting
- Word documents generated on test completion
- Screenshots captured at each step
- Failure screenshots with error context

### Multi-Browser Support
- Chrome (default)
- Firefox
- Headless/headed modes
- CI-optimized (headless in CI)

### CI/CD Ready
GitHub Actions workflow included for automated test execution.

---

## 📝 Writing New Tests

### 1. Add Test Data
Add a new entry to `test_data/testdata.json`:

```json
"new_test_case": {
  "product": "broadband",
  "postcode": "SW1A1AA",
  "housenum": "10, DOWNING STREET, LONDON, SW1A 2AA",
  "speed": "100 Mbps",
  "plan": "HBB",
  "planname": "Full Fibre 100",
  ...
}
```

### 2. Create Test Function
In the appropriate test file (e.g., `Tests/test_broadband_framework.py`):

```python
def test_new_test_case(page: Page, report):
    test_case_name = "new_test_case"
    report.start_test(test_case_name)
    data = get_test_data(test_case_name)

    landing = LandingPage(page, data, report)
    landing.accept_cookies()
    landing.check_availability()

    address = AddressPage(page, data, report)
    address.bbl_view_broadband_plans()

    plan = PlansPage(page, data, report)
    plan.select_plan()
    # ... continue flow
```

### 3. Add Locators (if needed)
Add new selectors to `test_data/locators.json` under the appropriate page.

---

## 🌐 CI/CD Pipeline

The `.github/workflows/playwright_pipeline.yml` runs:
1. Checkout repository
2. Setup Python 3.12
3. Install dependencies
4. Install Playwright browsers
5. Execute tests
6. Upload reports as artifacts

Triggered on:
- Push to `main`
- Pull requests to `main`

---

## 🛠️ Tech Stack

| Component | Version |
|-----------|---------|
| Python | 3.12+ |
| Playwright | 1.58.0 |
| pytest | 9.0.2 |
| pytest-playwright | 0.7.2 |
| python-docx | 1.2.0 |
| pytest-xdist | 3.8.0 |
| pytest-bdd | 8.1.0 |

---

## 📁 Configuration Files

| File | Purpose |
|------|---------|
| `conftest.py` | Pytest fixtures, browser config, URL routing, report fixture |
| `requirements.txt` | Python dependencies |
| `test_data/testdata.json` | Test case data (postcodes, plans, checkout info) |
| `test_data/locators.json` | CSS/XPath selectors per page |
| `.github/workflows/playwright_pipeline.yml` | CI/CD pipeline |

---

## 🤝 Contributing

1. Create a feature branch
2. Add test data to `test_data/testdata.json`
3. Add locators to `test_data/locators.json` if needed
4. Write test in appropriate `Tests/` file
5. Run locally to verify
6. Submit PR

---

## 📄 License

Internal Vodafone automation framework.