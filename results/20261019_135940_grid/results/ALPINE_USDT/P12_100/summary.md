# EMA Hourly Continuation — ALPINE/USDT P12_100

**Symbol:** ALPINE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.5684 |
| net_win_rate | 0.4504 |
| gross_profit_factor | 0.8280 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -3.4567 |
| sortino_ratio | -0.9595 |
| max_drawdown | 0.6985 |
| cagr | -0.3675 |
| net_avg_win | 50.8472 |
| net_avg_loss | -73.3096 |
| avg_hold_time_bars | 40.0916 |
| exposure | 0.7162 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
