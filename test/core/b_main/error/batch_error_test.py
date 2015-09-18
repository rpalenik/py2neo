#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright 2011-2014, Nigel Small
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from py2neo import GraphError
from py2neo.http.batch import WriteBatch, CypherJob, BatchError


def test_invalid_syntax_raises_cypher_error(graph):
    batch = WriteBatch(graph)
    batch.append(CypherJob("X"))
    try:
        batch.submit()
    except BatchError as error:
        assert isinstance(error, BatchError)
        cause = error.__cause__
        assert isinstance(cause, GraphError)
        assert cause.__class__.__name__ == "SyntaxException"
        assert cause.exception == "SyntaxException"
        assert cause.fullname in [None, "org.neo4j.cypher.SyntaxException"]
    else:
        assert False
