# EMA Hourly Continuation — CFX/USDT P12_21

**Symbol:** CFX/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.8604 |
| net_win_rate | 0.5551 |
| gross_profit_factor | 1.2314 |
| gross_win_rate | 0.5551 |
| sharpe_ratio | -0.7234 |
| sortino_ratio | -0.1736 |
| max_drawdown | 0.2575 |
| cagr | -0.0772 |
| net_avg_win | 74.5638 |
| net_avg_loss | -108.1470 |
| avg_hold_time_bars | 5.4412 |
| exposure | 0.0673 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
