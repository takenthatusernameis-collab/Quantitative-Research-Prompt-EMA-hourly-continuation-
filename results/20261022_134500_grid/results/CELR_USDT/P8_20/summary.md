# EMA Hourly Continuation — CELR/USDT P8_20

**Symbol:** CELR/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1618 |
| net_profit_factor | 0.3397 |
| net_win_rate | 0.4159 |
| gross_profit_factor | 0.8233 |
| gross_win_rate | 0.4425 |
| sharpe_ratio | -11.6794 |
| sortino_ratio | -6.6375 |
| max_drawdown | 0.9997 |
| cagr | -0.9621 |
| net_avg_win | 7.6431 |
| net_avg_loss | -16.0224 |
| avg_hold_time_bars | 3.2954 |
| exposure | 0.2413 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
