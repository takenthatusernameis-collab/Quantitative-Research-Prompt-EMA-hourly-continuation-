# EMA Hourly Continuation — BSV/USDT P89_200

**Symbol:** BSV/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.5756 |
| net_win_rate | 0.4266 |
| gross_profit_factor | 0.7608 |
| gross_win_rate | 0.4266 |
| sharpe_ratio | -3.0594 |
| sortino_ratio | -0.7427 |
| max_drawdown | 0.5768 |
| cagr | -0.2900 |
| net_avg_win | 62.5730 |
| net_avg_loss | -80.8913 |
| avg_hold_time_bars | 14.6621 |
| exposure | 0.1953 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
