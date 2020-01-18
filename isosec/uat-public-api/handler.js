'use strict';

module.exports.endpoint = (event, context, callback) => {
  const response = {
    statusCode: 200,
    body: 'Isosec Virtual Smartcard Store',
  };

  callback(null, response);
};
