import styled from "styled-components";
import {fractions} from "../../conts";

export const Split = styled.div`
  display: grid;
  gap: ${(props) => props.gutter};
  grid-template-columns: ${(props) =>
    fractions[props.fraction] ?? fractions["1/2"]};
`;
