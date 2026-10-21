# EMA Hourly Continuation — XRP/USDT P144_200

**Symbol:** XRP/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 185 |
| net_profit_factor | 0.5363 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 0.8564 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -2.5274 |
| sortino_ratio | -0.4939 |
| max_drawdown | 0.4412 |
| cagr | -0.2017 |
| net_avg_win | 58.1019 |
| net_avg_loss | -94.1070 |
| avg_hold_time_bars | 7.2703 |
| exposure | 0.0611 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
