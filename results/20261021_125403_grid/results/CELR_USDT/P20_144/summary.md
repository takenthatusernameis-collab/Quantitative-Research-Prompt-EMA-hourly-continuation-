# EMA Hourly Continuation — CELR/USDT P20_144

**Symbol:** CELR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.6935 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 0.8473 |
| gross_win_rate | 0.4560 |
| sharpe_ratio | -2.3555 |
| sortino_ratio | -0.6552 |
| max_drawdown | 0.5592 |
| cagr | -0.2609 |
| net_avg_win | 68.5995 |
| net_avg_loss | -82.9039 |
| avg_hold_time_bars | 32.9301 |
| exposure | 0.5752 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
