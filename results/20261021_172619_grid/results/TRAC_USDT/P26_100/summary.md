# EMA Hourly Continuation — TRAC/USDT P26_100

**Symbol:** TRAC/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.8332 |
| net_win_rate | 0.5109 |
| gross_profit_factor | 1.0418 |
| gross_win_rate | 0.5109 |
| sharpe_ratio | -1.2006 |
| sortino_ratio | -0.3690 |
| max_drawdown | 0.4168 |
| cagr | -0.1577 |
| net_avg_win | 74.7466 |
| net_avg_loss | -93.7184 |
| avg_hold_time_bars | 14.5961 |
| exposure | 0.3039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
