# EMA Hourly Continuation — LINK/USDT P50_89

**Symbol:** LINK/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.7421 |
| net_win_rate | 0.5034 |
| gross_profit_factor | 1.0206 |
| gross_win_rate | 0.5034 |
| sharpe_ratio | -1.6131 |
| sortino_ratio | -0.3961 |
| max_drawdown | 0.3736 |
| cagr | -0.1660 |
| net_avg_win | 71.6587 |
| net_avg_loss | -97.8901 |
| avg_hold_time_bars | 8.2329 |
| exposure | 0.1093 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
