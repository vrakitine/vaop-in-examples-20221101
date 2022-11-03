def getVaScript():
    va_script = {
      "Action__start":{
          "_agent_position":{
              "en-US":"In Init block of VA-box",
              "ru-RU":"В блоке Init VA-box"
          },
          "_action_description":{
              "_010":"--> init action"
          },
          "Direction_green":"Action__add_to_sum",  "_010":" > 0)",
          "Direction_blue":"Action__do_nothing",  "_010":" <= 0",
          "Direction_brown":"Action__met_array",  "_010":"Met an array",
          "Direction_red":"Action_9000",  "_010":"The end of array"
      },
      "Action__add_to_sum":{
          "_agent_position":{
              "en-US":"The v-agent is adding current element of array to the sum_01",
              "ru-RU":"v-agent добавляет текущий элемент массива к sum_01"
          },
          "_action_description":{
              "_010":"empty"
          },
          "Direction_green":"Action__add_to_sum",  "_010":" > 0)",
          "Direction_blue":"Action__do_nothing",  "_010":" <= 0",
          "Direction_brown":"Action__met_array",  "_010":"Met an array",
          "Direction_red":"Action_9000",  "_010":"The end of array"
      },
      "Action__do_nothing":{
          "_agent_position":{
              "en-US":"The v-agent is skipping the current element of array",
              "ru-RU":"v-agent пропускает текущий элемент массива"
          },
          "_action_description":{
              "_010":"empty"
          },
          "Direction_green":"Action__add_to_sum",  "_010":" > 0)",
          "Direction_blue":"Action__do_nothing",  "_010":" <= 0",
          "Direction_brown":"Action__met_array",  "_010":"Met an array",
          "Direction_red":"Action_9000",  "_010":"The end of array"
      },      
      "Action__met_array":{
          "_agent_position":{
              "en-US":"The v-agent is skipping the current element of array",
              "ru-RU":"v-agent пропускает текущий элемент массива"
          },
          "_action_description":{
              "_010":"empty"
          },
          "Direction_green":"Action__add_to_sum",  "_010":" > 0)",
          "Direction_blue":"Action__do_nothing",  "_010":" <= 0",
          "Direction_brown":"Action__met_array",  "_010":"Met an array",
          "Direction_red":"Action_9000",  "_010":"The end of array"
      },    
      "Action_9000":{
          "_agent_position":{
              "en-US":"The v-agent found the end of array",
              "ru-RU":"v-agent нашел конец массива"
          },
          "_action_description":{
              "_010":"empty"
          },
          "Direction_green":"Action_END",  "_010":" > 0",
          "Direction_blue":"Action_END",  "_010":" <= 0",
          "Direction_brown":"Action__met_array",  "_010":"Met an array",
          "Direction_red":"Action_END",  "_010":"The end of array"
      }
    }

    return va_script
    