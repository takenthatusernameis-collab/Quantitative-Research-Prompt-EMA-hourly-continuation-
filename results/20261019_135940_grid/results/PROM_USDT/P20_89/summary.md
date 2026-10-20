# EMA Hourly Continuation — PROM/USDT P20_89

**Symbol:** PROM/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 735 |
| net_profit_factor | 0.5037 |
| net_win_rate | 0.4327 |
| gross_profit_factor | 0.8828 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -6.2074 |
| sortino_ratio | -2.3369 |
| max_drawdown | 0.9465 |
| cagr | -0.6867 |
| net_avg_win | 30.1897 |
| net_avg_loss | -45.7031 |
| avg_hold_time_bars | 11.5864 |
| exposure | 0.3871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
