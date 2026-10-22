# EMA Hourly Continuation — AVA/USDT P26_100

**Symbol:** AVA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.9224 |
| net_win_rate | 0.5441 |
| gross_profit_factor | 1.1698 |
| gross_win_rate | 0.5441 |
| sharpe_ratio | -0.4307 |
| sortino_ratio | -0.1330 |
| max_drawdown | 0.3277 |
| cagr | -0.0647 |
| net_avg_win | 74.4921 |
| net_avg_loss | -96.3601 |
| avg_hold_time_bars | 15.5947 |
| exposure | 0.3218 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
