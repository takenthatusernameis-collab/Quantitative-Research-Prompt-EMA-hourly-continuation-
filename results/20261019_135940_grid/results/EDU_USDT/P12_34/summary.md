# EMA Hourly Continuation — EDU/USDT P12_34

**Symbol:** EDU/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1304 |
| net_profit_factor | 0.4769 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.7952 |
| gross_win_rate | 0.4525 |
| sharpe_ratio | -7.8604 |
| sortino_ratio | -4.0110 |
| max_drawdown | 0.9922 |
| cagr | -0.8523 |
| net_avg_win | 15.7297 |
| net_avg_loss | -26.0141 |
| avg_hold_time_bars | 4.6679 |
| exposure | 0.2754 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
