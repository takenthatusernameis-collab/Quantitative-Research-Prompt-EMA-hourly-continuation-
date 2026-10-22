# EMA Hourly Continuation — SHIB/USDT P20_34

**Symbol:** SHIB/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1114 |
| net_profit_factor | 0.2971 |
| net_win_rate | 0.4048 |
| gross_profit_factor | 0.8122 |
| gross_win_rate | 0.4443 |
| sharpe_ratio | -12.0580 |
| sortino_ratio | -5.7599 |
| max_drawdown | 0.9995 |
| cagr | -0.9526 |
| net_avg_win | 9.3687 |
| net_avg_loss | -21.4488 |
| avg_hold_time_bars | 2.3833 |
| exposure | 0.1207 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
