# Flask Template Project

This is a Flask template project. You can use this as a starting point for your web application.

## Installation

1. Clone the repository:

   ```bash
   git clone <your-repository-url>
   ```


2. Create a virtual environment:

   ```bash
   pyrton3 -m venv venv
   ```

3. Activate the virtual environment
   ```bash
   source venv/bin/activate # On Windows use 'venv\Scripts\activate'
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```


## Environment Variables

Before you start the application, you need to set up the environment variables. Create a `.env` file in the root directory of the project and add the following variables:

```properties
SECRET_KEY='your_secret_key'
DATABASE_URI="mysql+mysqlconnector://username:password@localhost:3306/database_name"
JWT_SECRET_KEY='your_jwt_secret_key'
```

## Usage

1. Set up the database:

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

2. Run the application:

   ```bash
   flask run
   ```

3. Open your web browser and visit `http://localhost:5000` to view the application.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m "Add your commit message here"
   ```

4. Push your changes to your forked repository:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Open a pull request to the original repository.

