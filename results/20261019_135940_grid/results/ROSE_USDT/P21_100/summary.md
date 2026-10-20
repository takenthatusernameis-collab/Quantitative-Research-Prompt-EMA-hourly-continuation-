# EMA Hourly Continuation — ROSE/USDT P21_100

**Symbol:** ROSE/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 677 |
| net_profit_factor | 0.6904 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9790 |
| gross_win_rate | 0.4860 |
| sharpe_ratio | -3.4262 |
| sortino_ratio | -1.2613 |
| max_drawdown | 0.7920 |
| cagr | -0.4466 |
| net_avg_win | 52.9284 |
| net_avg_loss | -71.2001 |
| avg_hold_time_bars | 14.2157 |
| exposure | 0.4375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
