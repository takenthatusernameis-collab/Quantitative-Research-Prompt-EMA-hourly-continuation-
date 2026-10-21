# EMA Hourly Continuation — XPR/USDT P26_100

**Symbol:** XPR/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 682 |
| net_profit_factor | 0.4200 |
| net_win_rate | 0.4223 |
| gross_profit_factor | 0.7707 |
| gross_win_rate | 0.4267 |
| sharpe_ratio | -7.2474 |
| sortino_ratio | -2.6331 |
| max_drawdown | 0.9686 |
| cagr | -0.7459 |
| net_avg_win | 24.3335 |
| net_avg_loss | -42.3542 |
| avg_hold_time_bars | 9.4589 |
| exposure | 0.2932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
