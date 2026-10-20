# EMA Hourly Continuation — IO/USDT P12_200

**Symbol:** IO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.6229 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 0.8783 |
| gross_win_rate | 0.4675 |
| sharpe_ratio | -3.0917 |
| sortino_ratio | -0.8738 |
| max_drawdown | 0.6550 |
| cagr | -0.3442 |
| net_avg_win | 58.1438 |
| net_avg_loss | -81.1148 |
| avg_hold_time_bars | 39.9532 |
| exposure | 0.7447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
