# EMA Hourly Continuation — ASTR/USDT P8_55

**Symbol:** ASTR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.7892 |
| net_win_rate | 0.5079 |
| gross_profit_factor | 1.0556 |
| gross_win_rate | 0.5079 |
| sharpe_ratio | -2.2676 |
| sortino_ratio | -0.8530 |
| max_drawdown | 0.6431 |
| cagr | -0.3259 |
| net_avg_win | 67.0435 |
| net_avg_loss | -87.6870 |
| avg_hold_time_bars | 16.1645 |
| exposure | 0.5069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
