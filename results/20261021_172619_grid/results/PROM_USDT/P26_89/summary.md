# EMA Hourly Continuation — PROM/USDT P26_89

**Symbol:** PROM/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.6053 |
| net_win_rate | 0.4484 |
| gross_profit_factor | 0.8300 |
| gross_win_rate | 0.4505 |
| sharpe_ratio | -3.4585 |
| sortino_ratio | -1.0684 |
| max_drawdown | 0.7158 |
| cagr | -0.3908 |
| net_avg_win | 51.2499 |
| net_avg_loss | -68.8390 |
| avg_hold_time_bars | 13.5221 |
| exposure | 0.2920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
