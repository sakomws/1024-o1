# 1024-o1

![Architecture](images/architecture.jpg)

### Description
A brief introduction to your project, explaining what it does, its purpose, and the problem it solves.

### Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/sakomws/1024-o1.git
    ```

3. Install dependencies:

    ```
    cd 1024-o1-storefront
    yarn install
    ```
    ```
    Storefront admin:
    ```
    cd 1024-o1-admin
    yarn install
    ```

    ```
    cd 1024-o1-admin
    pip install -r requirements.txt
    python main.py
    ```


### Usage

1. Run the project:

    ```
    yarn dev
    ```

2. Open your browser and navigate to `http://localhost:` (or the port specified in the project).

### Features
- Data collection
  - User profile:
    - user data
    - 3rd party data
    - public data: linkedin etc.
    - synthetic data
    
- accuracy: intent, content and context
- metadata: create tags, labels for data using llms
- classify actions for realtime and non-realtime to predict user behave and calculate lifetime value
- generate report for business to maximize customer satisfaction and revenue and minimize time to deliver

### Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a pull request.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
