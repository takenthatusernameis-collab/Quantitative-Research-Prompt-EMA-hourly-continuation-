# EMA Hourly Continuation — BLUR/USDT P8_144

**Symbol:** BLUR/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.8300 |
| net_win_rate | 0.5307 |
| gross_profit_factor | 1.1633 |
| gross_win_rate | 0.5430 |
| sharpe_ratio | -1.0607 |
| sortino_ratio | -0.3028 |
| max_drawdown | 0.3580 |
| cagr | -0.1361 |
| net_avg_win | 69.7674 |
| net_avg_loss | -95.0618 |
| avg_hold_time_bars | 42.9730 |
| exposure | 0.7914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
