const docx = require('docx');
const { Document, Paragraph, TextRun, HeadingLevel, AlignmentType, Packer, BorderStyle, Table, TableRow, TableCell, WidthType, ShadingType, ImageRun, PageBreak, PositionalTabAlignment, PositionalTabLeader } = docx;

// Helper function to create a section heading
const createSectionHeading = (text) => {
  return new Paragraph({
    text: text,
    heading: HeadingLevel.HEADING_1,
    thematicBreak: true,
    spacing: { before: 300, after: 100 },
    border: {
      bottom: {
        color: "2563EB",
        space: 1,
        style: BorderStyle.SINGLE,
        size: 12,
      },
    },
  });
};

// Helper function to create a subsection heading
const createSubsectionHeading = (text) => {
  return new Paragraph({
    text: text,
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 200, after: 50 },
    border: {
      bottom: {
        color: "3B82F6",
        space: 1,
        style: BorderStyle.SINGLE,
        size: 6,
      },
    },
  });
};

// Helper function to create body text
const createBodyText = (text, bold = false, italic = false, size = 22) => {
  return new Paragraph({
    children: [
      new TextRun({
        text: text,
        bold: bold,
        italic: italic,
        size: size,
        font: "Calibri",
      }),
    ],
    spacing: { after: 100 },
  });
};

// Helper function to create bullet points
const createBulletPoint = (text, level = 0) => {
  return new Paragraph({
    text: text,
    bullet: {
      level: level,
    },
    spacing: { after: 60 },
  });
};

// Helper function to create skill tag paragraph
const createSkillParagraph = (skills) => {
  return new Paragraph({
    children: skills.map((skill, index) => {
      const isLast = index === skills.length - 1;
      return new TextRun({
        text: skill + (isLast ? "" : "  |  "),
        size: 22,
        font: "Calibri",
        color: "2563EB",
      });
    }),
    spacing: { after: 120 },
  });
};

// Helper function to create experience entry
const createExperienceEntry = (title, company, location, dates, bullets) => {
  const paragraphs = [
    new Paragraph({
      children: [
        new TextRun({ text: title, bold: true, size: 24, font: "Calibri", color: "1E293B" }),
        new TextRun({ text: "  |  ", size: 22, font: "Calibri", color: "64748B" }),
        new TextRun({ text: company, size: 22, font: "Calibri", color: "1E293B" }),
        new TextRun({ text: "  |  ", size: 22, font: "Calibri", color: "64748B" }),
        new TextRun({ text: location, size: 22, font: "Calibri", color: "64748B" }),
        new TextRun({ text: "  |  ", size: 22, font: "Calibri", color: "64748B" }),
        new TextRun({ text: dates, size: 22, font: "Calibri", color: "64748B" }),
      ],
      spacing: { after: 80 },
    }),
  ];

  bullets.forEach(bullet => {
    paragraphs.push(new Paragraph({
      text: bullet,
      bullet: { level: 0 },
      spacing: { after: 60 },
    }));
  });

  paragraphs.push(new Paragraph({ text: "", spacing: { after: 100 } }));
  return paragraphs;
};

const doc = new Document({
  sections: [
    {
      properties: {
        page: {
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
        },
      },
      children: [
        // HEADER SECTION
        new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({
              text: "MITESH PATEL",
              bold: true,
              size: 40,
              font: "Calibri",
              color: "1E293B",
            }),
          ],
          spacing: { after: 50 },
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({
              text: "Senior QA Automation Engineer | SDET | Test Automation Architect",
              size: 26,
              font: "Calibri",
              color: "2563EB",
              italic: true,
            }),
          ],
          spacing: { after: 100 },
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({
              text: "📍 London, UK  |  📧 mitesh.patel@email.com  |  📱 +44 7XXX XXXXXX  |  🔗 linkedin.com/in/mitesh-patel  |  💻 github.com/mitesh-patel",
              size: 22,
              font: "Calibri",
              color: "475569",
            }),
          ],
          spacing: { after: 200 },
        }),

        // PROFESSIONAL SUMMARY
        createSectionHeading("PROFESSIONAL SUMMARY"),
        createBodyText(
          "Results-driven Senior QA Automation Engineer with 8+ years of experience designing, developing, and maintaining enterprise-grade test automation frameworks. Expert in Playwright (TypeScript/JavaScript), Python (pytest, Behave), and modern CI/CD pipelines. Proven track record of reducing regression test execution time by 70%+, achieving 90%+ test coverage, and mentoring cross-functional teams. Strong advocate for Shift-Left testing, BDD/TDD practices, and quality engineering culture. Experience across FinTech, Telecom, and E-commerce domains with expertise in API testing, performance testing, and cloud-based test execution."
        ),

        // TECHNICAL SKILLS
        createSectionHeading("TECHNICAL SKILLS"),
        createSubsectionHeading("Test Automation Frameworks & Tools"),
        createSkillParagraph([
          "Playwright (TypeScript/JavaScript)", "Selenium WebDriver (Java/Python)",
          "Cypress", "Appium", "WebdriverIO", "TestCafe"
        ]),
        createSubsectionHeading("Programming Languages"),
        createSkillParagraph([
          "Python (Advanced)", "TypeScript/JavaScript (Advanced)",
          "Java (Intermediate)", "C# (Intermediate)", "SQL"
        ]),
        createSubsectionHeading("BDD/TDD & Test Frameworks"),
        createSkillParagraph([
          "pytest (Advanced)", "Behave/Cucumber (Gherkin)",
          "JUnit/TestNG", "Jest", "Vitest", "Playwright Test Runner"
        ]),
        createSubsectionHeading("CI/CD & DevOps"),
        createSkillParagraph([
          "GitHub Actions", "GitLab CI/CD", "Jenkins", "Azure DevOps",
          "CircleCI", "Docker", "Kubernetes", "AWS/GCP"
        ]),
        createSubsectionHeading("API & Performance Testing"),
        createSkillParagraph([
          "Postman/Newman", "REST Assured", "k6", "JMeter", "Locust", "Artillery"
        ]),
        createSubsectionHeading("Databases & Messaging"),
        createSkillParagraph([
          "PostgreSQL", "MySQL", "MongoDB", "Redis", "Kafka", "RabbitMQ"
        ]),
        createSubsectionHeading("Cloud & Infrastructure"),
        createSkillParagraph([
          "AWS (EC2, ECS, Lambda, S3)", "GCP", "Azure", "Terraform", "Helm"
        ]),
        createSubsectionHeading("Version Control & Collaboration"),
        createSkillParagraph([
          "Git/GitHub/GitLab", "Jira", "Confluence", "Zephyr", "TestRail", "SonarQube"
        ]),

        // PROFESSIONAL EXPERIENCE
        createSectionHeading("PROFESSIONAL EXPERIENCE"),

        ...createExperienceEntry(
          "Senior QA Automation Engineer / SDET",
          "Vodafone Group",
          "London, UK (Hybrid)",
          "2022 – Present",
          [
            "Architected and implemented a comprehensive Playwright TypeScript automation framework from scratch, reducing regression suite execution from 6 hours to 45 minutes (87% improvement) across 1,200+ test cases",
            "Designed Page Object Model (POM) architecture with TypeScript, integrating with GitHub Actions for parallel execution across 10 browsers/devices, achieving 92% cross-browser test coverage",
            "Built custom pytest-BDD framework for API testing with 500+ automated test scenarios covering REST, GraphQL, and gRPC services, integrated with Postman/Newman for contract testing",
            "Implemented visual regression testing using Playwright's snapshot comparison, catching 40+ UI regressions per release cycle before production deployment",
            "Mentored 5 junior QA engineers on Playwright, TypeScript, pytest, and CI/CD best practices; conducted weekly workshops on test automation patterns and debugging techniques",
            "Established Shift-Left testing practices: integrated automated security scanning (OWASP ZAP), accessibility testing (axe-core), and performance budgets into PR pipeline",
            "Reduced flaky test rate from 15% to <0.5% through robust wait strategies, test data management, and test isolation patterns using Playwright fixtures and pytest fixtures",
            "Collaborated with DevOps to implement test execution in Kubernetes clusters using Helm charts, enabling scalable parallel test runs for 2,000+ daily test executions"
          ]
        ),

        ...createExperienceEntry(
          "QA Automation Lead",
          "Barclays / FinTech Client",
          "London, UK",
          "2019 – 2022",
          [
            "Led a team of 8 QA engineers in building end-to-end test automation for core banking platform processing £2B+ daily transactions",
            "Developed Python pytest framework with Behave for BDD, integrating with Jenkins and Azure DevOps; achieved 85% test coverage across 15 microservices",
            "Implemented contract testing with Pact for consumer-driven contracts, preventing 30+ breaking API changes from reaching production annually",
            "Designed and executed performance test suites using k6 and Locust, identifying bottlenecks that improved API response times by 40%",
            "Created test data management strategy using Docker Compose and synthetic data generation, reducing test environment setup from days to minutes",
            "Championed quality gates: integrated SonarQube, OWASP dependency check, and mutation testing (Stryker) into CI pipeline"
          ]
        ),

        ...createExperienceEntry(
          "Senior QA Automation Engineer",
          "Sky / Telecom",
          "London, UK",
          "2016 – 2019",
          [
            "Built Selenium WebDriver + Java + TestNG framework for customer-facing portal serving 12M+ users; reduced manual regression from 3 weeks to 2 days",
            "Developed mobile test automation using Appium for iOS/Android native and hybrid apps, integrated with BrowserStack for 50+ device coverage",
            "Implemented API test automation with REST Assured and Python requests, covering 200+ endpoints with data-driven testing approach",
            "Established test reporting dashboard using Allure Report and Grafana, providing real-time visibility into test execution metrics for stakeholders",
            "Introduced Git branching strategy and code review process for test code, improving test code quality and maintainability"
          ]
        ),

        // EDUCATION & CERTIFICATIONS
        createSectionHeading("EDUCATION & CERTIFICATIONS"),
        createSubsectionHeading("Education"),
        createBodyText("MSc Computer Science (Distinction)", true),
        createBodyText("University of London, UK | 2014 – 2016"),
        createBodyText("BSc Information Technology", true),
        createBodyText("Mumbai University, India | 2010 – 2013"),

        createSubsectionHeading("Professional Certifications"),
        createBulletPoint("Playwright Certified Professional – Microsoft (2024)"),
        createBulletPoint("AWS Certified Solutions Architect – Associate (2023)"),
        createBulletPoint("ISTQB Advanced Test Automation Engineer (2022)"),
        createBulletPoint("Certified Kubernetes Application Developer (CKAD) – CNCF (2023)"),
        createBulletPoint("Postman API Testing Certified (2023)"),
        createBulletPoint("Certified Scrum Master (CSM) – Scrum Alliance (2021)"),

        // KEY PROJECTS
        createSectionHeading("KEY PROJECTS & ACHIEVEMENTS"),

        createSubsectionHeading("Playwright Enterprise Framework (Open Source Contribution)"),
        createBulletPoint("Contributed to Playwright core: fixed race condition in trace viewer (PR #18,432)"),
        createBulletPoint("Created playwright-pytest-plugin: pytest integration for Playwright with 2.5k+ GitHub stars"),
        createBulletPoint("Authored 'Advanced Playwright Patterns' blog series (15 articles, 50k+ reads)"),

        createSubsectionHeading("Test Automation Center of Excellence"),
        createBulletPoint("Established CoE at Vodafone: standardized frameworks, templates, and guidelines across 12 teams"),
        createBulletPoint("Created reusable component library: 50+ Page Objects, 30+ API clients, 20+ custom fixtures"),
        createBulletPoint("Reduced onboarding time for new QA hires from 4 weeks to 1 week through structured training program"),

        createSubsectionHeading("Continuous Quality Platform"),
        createBulletPoint("Built unified dashboard aggregating test results, coverage, flakiness, and performance metrics"),
        createBulletPoint("Implemented ML-based flaky test detection reducing false positives by 95%"),
        createBulletPoint("Integrated with Slack/MS Teams for real-time test failure notifications with root cause analysis"),

        // TECHNICAL PUBLICATIONS & SPEAKING
        createSectionHeading("TECHNICAL PUBLICATIONS & SPEAKING"),
        createBulletPoint("Speaker: 'Modern Test Automation with Playwright' – QA London Conference 2024 (300+ attendees)"),
        createBulletPoint("Speaker: 'pytest Advanced Patterns for Enterprise' – PyCon UK 2023"),
        createBulletPoint("Author: 'Building Scalable Test Automation Frameworks' – Medium publication (25k+ reads)"),
        createBulletPoint("Maintainer: playwright-python-template (1.2k stars) – production-ready starter kit"),

        // FOOTER
        new Paragraph({
          text: "",
          spacing: { before: 300 },
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({
              text: "References available upon request  |  Portfolio: github.com/mitesh-patel  |  Blog: miteshpatel.tech",
              size: 20,
              font: "Calibri",
              color: "64748B",
              italic: true,
            }),
          ],
        }),
      ],
    },
  ],
});

// Write the document
Packer.toBuffer(doc).then((buffer) => {
  const fs = require('fs');
  fs.writeFileSync('Mitesh_Patel_QA_Automation_Resume.docx', buffer);
  console.log('Resume created successfully: Mitesh_Patel_QA_Automation_Resume.docx');
}).catch((error) => {
  console.error('Error creating resume:', error);
});