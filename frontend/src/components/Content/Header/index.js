import styled from "styled-components";
import { Pad } from "../../Pad";
import { Center } from "../../Center";

const ComponentHeader = styled(Center).attrs(() => ({
  as: Pad,
  padding: ["0", "0", "1rem"],
  align: "center",
  justify: "center",
}))`
  border-block-end: 1px solid rgb(229, 229, 229);
`;

const Title = styled.h2`
  margin: 0.5rem 0;
`;
const SubTitle = styled.span`
  color: gray;
`;
export default function Header({ meterById }) {
  return (
    <ComponentHeader>
      <Title>{meterById?.name}</Title>
      <SubTitle>{meterById?.type}</SubTitle>
    </ComponentHeader>
  );
}
