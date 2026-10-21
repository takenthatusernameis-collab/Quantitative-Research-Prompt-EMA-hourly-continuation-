# EMA Hourly Continuation — CAKE/USDT P34_55

**Symbol:** CAKE/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.6154 |
| net_win_rate | 0.4856 |
| gross_profit_factor | 0.9391 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -2.6470 |
| sortino_ratio | -0.6728 |
| max_drawdown | 0.5583 |
| cagr | -0.2648 |
| net_avg_win | 56.6564 |
| net_avg_loss | -86.9128 |
| avg_hold_time_bars | 6.4665 |
| exposure | 0.0920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
