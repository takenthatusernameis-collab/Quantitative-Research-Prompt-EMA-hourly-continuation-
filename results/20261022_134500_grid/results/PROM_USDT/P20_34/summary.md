# EMA Hourly Continuation — PROM/USDT P20_34

**Symbol:** PROM/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1147 |
| net_profit_factor | 0.3740 |
| net_win_rate | 0.3976 |
| gross_profit_factor | 0.8477 |
| gross_win_rate | 0.4342 |
| sharpe_ratio | -11.3378 |
| sortino_ratio | -5.4521 |
| max_drawdown | 0.9992 |
| cagr | -0.9401 |
| net_avg_win | 13.0897 |
| net_avg_loss | -23.0975 |
| avg_hold_time_bars | 3.3104 |
| exposure | 0.1726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
