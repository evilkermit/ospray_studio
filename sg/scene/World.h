// Copyright 2009-2020 Intel Corporation
// SPDX-License-Identifier: Apache-2.0

#pragma once

#include "../Node.h"
#include "lights/Light.h"

namespace ospray {
  namespace sg {

  struct OSPSG_INTERFACE World : public OSPNode<cpp::World, NodeType::WORLD>
  {
    World();
    ~World() override = default;

    std::vector<cpp::Light> lightObjects = {};

    virtual void preCommit() override;
    virtual void postCommit() override;
  };

  }  // namespace sg
} // namespace ospray
