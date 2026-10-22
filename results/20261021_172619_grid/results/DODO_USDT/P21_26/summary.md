# EMA Hourly Continuation — DODO/USDT P21_26

**Symbol:** DODO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.5668 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8249 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -2.9361 |
| sortino_ratio | -0.7087 |
| max_drawdown | 0.5606 |
| cagr | -0.2782 |
| net_avg_win | 56.4110 |
| net_avg_loss | -82.9440 |
| avg_hold_time_bars | 5.4371 |
| exposure | 0.0704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
