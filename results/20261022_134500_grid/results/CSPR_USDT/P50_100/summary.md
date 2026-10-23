# EMA Hourly Continuation — CSPR/USDT P50_100

**Symbol:** CSPR/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 900 |
| net_profit_factor | 0.3997 |
| net_win_rate | 0.4033 |
| gross_profit_factor | 0.7215 |
| gross_win_rate | 0.4067 |
| sharpe_ratio | -8.4692 |
| sortino_ratio | -3.5972 |
| max_drawdown | 0.9884 |
| cagr | -0.8299 |
| net_avg_win | 18.1295 |
| net_avg_loss | -30.6591 |
| avg_hold_time_bars | 4.4200 |
| exposure | 0.1808 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
