# EMA Hourly Continuation — THETA/USDT P55_89

**Symbol:** THETA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.4807 |
| net_win_rate | 0.4642 |
| gross_profit_factor | 0.8580 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -5.6844 |
| sortino_ratio | -2.0809 |
| max_drawdown | 0.9241 |
| cagr | -0.6381 |
| net_avg_win | 27.4463 |
| net_avg_loss | -49.4622 |
| avg_hold_time_bars | 3.8672 |
| exposure | 0.1178 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
