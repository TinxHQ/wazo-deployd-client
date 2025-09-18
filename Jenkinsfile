pipeline {
  agent any
  triggers {
    githubPush()
    pollSCM('H H * * *')
  }
  parameters {
      choice(name: 'test', choices: ['yes','no'], description: 'Run all tests ?')
      choice(name: 'build_and_publish', choices: ['yes','no'], description: 'Build and publish assets ?')
  }
  environment {
    MAIL_RECIPIENTS = 'dev+tests-reports@wazo.community'
  }
  options {
    skipStagesAfterUnstable()
    timestamps()
    buildDiscarder(logRotator(numToKeepStr: '10'))
  }
  stages {
    stage('Linters') {
      when {
        expression {
          test == 'yes'
        }
      }
      steps {
        sh 'tox -e linters'
      }
    }
    stage('Unit tests') {
      when {
        expression {
          test == 'yes'
        }
      }
      steps {
        sh 'tox -e py39'
      }
    }
    stage('Debian build and deploy') {
      when {
        expression {
          build_and_publish == 'yes'
        }
      }
      steps {
        // This package is uploaded to public repo as a dependency to wazo-nestbox-plugin
        build job: 'build-package', parameters: [
          string(name: 'PACKAGE', value: "${env.JOB_NAME}"),
          string(name: 'VERSION', value: sh(script: 'wazo-version unstable', returnStdout: true).trim()),
          string(name: 'DEBIAN_REPOSITORY', value: 'engine'),
          string(name: 'DEBIAN_DISTRIBUTION', value: 'wazo-dev-bookworm'),
        ]
      }
    }
  }
  post {
    failure {
      emailext to: "${MAIL_RECIPIENTS}", subject: '${DEFAULT_SUBJECT}', body: '${DEFAULT_CONTENT}'
    }
    fixed {
      emailext to: "${MAIL_RECIPIENTS}", subject: '${DEFAULT_SUBJECT}', body: '${DEFAULT_CONTENT}'
    }
  }
}
