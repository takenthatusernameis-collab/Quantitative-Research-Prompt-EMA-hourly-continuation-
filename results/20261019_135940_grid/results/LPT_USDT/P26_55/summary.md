# EMA Hourly Continuation — LPT/USDT P26_55

**Symbol:** LPT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 964 |
| net_profit_factor | 0.4386 |
| net_win_rate | 0.4212 |
| gross_profit_factor | 0.7509 |
| gross_win_rate | 0.4492 |
| sharpe_ratio | -8.0814 |
| sortino_ratio | -3.5479 |
| max_drawdown | 0.9881 |
| cagr | -0.8230 |
| net_avg_win | 18.9917 |
| net_avg_loss | -31.5078 |
| avg_hold_time_bars | 4.4502 |
| exposure | 0.1950 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
