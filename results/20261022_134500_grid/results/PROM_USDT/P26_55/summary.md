# EMA Hourly Continuation — PROM/USDT P26_55

**Symbol:** PROM/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 956 |
| net_profit_factor | 0.4097 |
| net_win_rate | 0.4038 |
| gross_profit_factor | 0.8185 |
| gross_win_rate | 0.4362 |
| sharpe_ratio | -9.2784 |
| sortino_ratio | -4.0507 |
| max_drawdown | 0.9941 |
| cagr | -0.8705 |
| net_avg_win | 17.8746 |
| net_avg_loss | -29.5450 |
| avg_hold_time_bars | 4.5042 |
| exposure | 0.1957 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
