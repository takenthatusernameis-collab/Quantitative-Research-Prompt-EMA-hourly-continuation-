# EMA Hourly Continuation — AGLD/USDT P55_89

**Symbol:** AGLD/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.5906 |
| net_win_rate | 0.4395 |
| gross_profit_factor | 0.8214 |
| gross_win_rate | 0.4395 |
| sharpe_ratio | -3.7314 |
| sortino_ratio | -1.0990 |
| max_drawdown | 0.7302 |
| cagr | -0.3966 |
| net_avg_win | 54.9860 |
| net_avg_loss | -73.0128 |
| avg_hold_time_bars | 6.0674 |
| exposure | 0.1181 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
