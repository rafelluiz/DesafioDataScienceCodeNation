#!/usr/bin/env python

from flask import Flask, request, jsonify
from loguru import logger

from statsapi import data_store
from statsapi import operation


app = Flask(__name__)


@app.route('/data',methods=["POST"])
def save_data():
  logger.info(f'Saving data...')

  content = request.get_json()

  uuid = data_store.save(content['data'])

  logger.info(f'Data saved with UUID {uuid} sucessfully')

  return jsonify({"status":"sucess","message":"data saved successfully","uuid":uuid})


@app.route('/data/<uuid>',methods=['GET'])
def retrive_data(uuid):
  logger.info(f'Retrieving data associated with UUID{uuid} ...')

  try:
    store_data = data_store.get(uuid)
  except KeyError:
    logger.warning(f'Cannot retrieve data associeated with UUID {uuid}')

    return jsonify({'status':'failed','message':'data connot be retrived','data':[]})

  logger.info(f'Data associated whit UUID {uuid} retrived successfully')

  return jsonify(({'status':'success','message':'data retrieved successfuly','data':store_data}))



@app.route('/data/<uuid>/<operation>', methods=['GET'])
def process_operation(uuid, operation):
  logger.info(f'Processing operation {operation} on data associated with UUID {uuid}')

  try:
    store_data = data_store.get(uuid)

    operation_func = get_operation(operation)

    result = operation_func(store_data)
  except KeyError:
    logger.warning(f'Cannot retrieve data associeated with UUID {uuid}')

    return jsonify({'status': 'failed', 'message': 'data connot be retrived', 'result': None})

  except NoSuchOperationError:
    logger.warning(f'Cannot find opertatio {operation}')

    return jsonify({'status': 'failed', 'message': f'no such {operation} ', 'result': None})

  logger.info(f'Operation {operation} on data associated with UUID {uuid} finished successfuly')

  return jsonify({'status': 'success','message':'result completed','result':result})


def get_operation(operation_name):
  if operation_name == "min":
    return operation.op_min
  if operation_name == "max":
    return operation.op_max
  if operation_name == 'mean':
    return operation.op_mean
  else:
    raise NoSuchOperationError


class NoSuchOperationError(Exception):
  pass

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)