pipeline {
  agent any
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
      steps {
        sh 'tox -e linters'
      }
    }
    stage('Build and deploy') {
      steps {
        // This package is uploaded to public repo as a dependency to wazo-nestbox-plugin
        build job: 'build-package', parameters: [
          string(name: 'PACKAGE', value: "${env.JOB_NAME}"),
          string(name: 'VERSION', value: sh(script: 'wazo-version unstable', returnStdout: true).trim()),
          string(name: 'DEBIAN_REPOSITORY', value: 'engine'),
          string(name: 'DEBIAN_DISTRIBUTION', value: 'wazo-dev-buster'),
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
