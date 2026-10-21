# EMA Hourly Continuation — BLUR/USDT P50_55

**Symbol:** BLUR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 136 |
| net_profit_factor | 0.7388 |
| net_win_rate | 0.5294 |
| gross_profit_factor | 1.1436 |
| gross_win_rate | 0.5294 |
| sharpe_ratio | -1.1580 |
| sortino_ratio | -0.1943 |
| max_drawdown | 0.2681 |
| cagr | -0.0860 |
| net_avg_win | 79.7296 |
| net_avg_loss | -121.4022 |
| avg_hold_time_bars | 3.8456 |
| exposure | 0.0237 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
