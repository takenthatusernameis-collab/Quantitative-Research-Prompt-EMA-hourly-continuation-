# EMA Hourly Continuation — ATOM/USDT P50_55

**Symbol:** ATOM/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.1398 |
| net_win_rate | 0.3229 |
| gross_profit_factor | 0.6605 |
| gross_win_rate | 0.4051 |
| sharpe_ratio | -12.5080 |
| sortino_ratio | -5.0124 |
| max_drawdown | 0.9989 |
| cagr | -0.9338 |
| net_avg_win | 7.1225 |
| net_avg_loss | -24.2949 |
| avg_hold_time_bars | 1.9037 |
| exposure | 0.0611 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
