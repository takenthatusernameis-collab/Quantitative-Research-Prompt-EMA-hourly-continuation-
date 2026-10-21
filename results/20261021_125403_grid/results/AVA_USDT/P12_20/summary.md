# EMA Hourly Continuation — AVA/USDT P12_20

**Symbol:** AVA/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.6687 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 1.0062 |
| gross_win_rate | 0.5046 |
| sharpe_ratio | -2.2351 |
| sortino_ratio | -0.5842 |
| max_drawdown | 0.5170 |
| cagr | -0.2337 |
| net_avg_win | 59.2803 |
| net_avg_loss | -90.2834 |
| avg_hold_time_bars | 4.4407 |
| exposure | 0.0664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
