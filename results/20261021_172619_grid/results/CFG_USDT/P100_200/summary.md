# EMA Hourly Continuation — CFG/USDT P100_200

**Symbol:** CFG/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.7103 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.8602 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -1.7593 |
| sortino_ratio | -0.4273 |
| max_drawdown | 0.3953 |
| cagr | -0.1784 |
| net_avg_win | 70.2253 |
| net_avg_loss | -86.1938 |
| avg_hold_time_bars | 11.6130 |
| exposure | 0.1541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
