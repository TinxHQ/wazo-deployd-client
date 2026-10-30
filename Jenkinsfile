def execute_test = true
def execute_publish = false
def isPullRequest = env.CHANGE_ID != null
def isMaster = env.BRANCH_NAME == 'master'

pipeline {
  agent {
    label 'general-debian12-small'
  }
  parameters {
      choice(name: 'test', choices: ['yes','no'], description: 'Run all tests ? (Ignored for PR)')
      choice(name: 'build_and_publish', choices: ['yes','no'], description: 'Build and publish assets ? (Ignored for PR)')
  }
  environment {
    MAIL_RECIPIENTS = 'dev+tests-reports@wazo.community'
    PACKAGE_NAME = 'wazo-deployd-client'
  }
  options {
    skipStagesAfterUnstable()
    timestamps()
    buildDiscarder(logRotator(numToKeepStr: '10'))
  }
  stages {
    stage('Set variables') {
      steps {
        script {
          if (isMaster) {
            execute_test = params.test == 'yes'
            execute_publish = params.build_and_publish == 'yes'
          }
        }
      }
    }
    stage('Linters') {
      when {
        expression {
          execute_test
        }
      }
      steps {
        sh 'tox -e linters'
      }
    }
    stage('Unit tests') {
      when {
        expression {
          execute_test
        }
      }
      steps {
        sh 'tox -e py311'
      }
    }
    stage('Debian build and deploy') {
      when {
        expression {
          execute_publish
        }
      }
      steps {
        build job: 'build-debian-package', parameters: [
          string(name: 'PACKAGE', value: "${env.PACKAGE_NAME}"),
          string(name: 'VERSION', value: sh(script: 'wazo-version unstable', returnStdout: true).trim()),
          string(name: 'DEBIAN_REPOSITORY', value: 'enterprise'),
          string(name: 'DEBIAN_DISTRIBUTION', value: 'enterprise-dev-bookworm'),
        ]
      }
    }
  }
  post {
    success {
      script {
        if (isPullRequest) {
          pullRequest.comment(":heavy_check_mark: [Build](${BUILD_URL}) SUCCEEDED.\n\n* [Job overview](${JOB_URL})\n* [Console output](${BUILD_URL}console)")
        }
      }
    }
    failure {
      script {
        if (isPullRequest) {
          pullRequest.comment(":x: [Build](${BUILD_URL}) FAILED.\n\n* [Job overview](${JOB_URL})\n* [Console output](${BUILD_URL}console)")
        }
        if (isMaster) {
          emailext to: "${MAIL_RECIPIENTS}", subject: '${DEFAULT_SUBJECT}', body: '${DEFAULT_CONTENT}'
        }
      }
    }
    fixed {
      script {
        if (isMaster) {
          emailext to: "${MAIL_RECIPIENTS}", subject: '${DEFAULT_SUBJECT}', body: '${DEFAULT_CONTENT}'
        }
      }
    }
  }
}
