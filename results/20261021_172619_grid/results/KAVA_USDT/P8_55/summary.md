# EMA Hourly Continuation — KAVA/USDT P8_55

**Symbol:** KAVA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 747 |
| net_profit_factor | 0.7238 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 0.9939 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -3.5870 |
| sortino_ratio | -1.3947 |
| max_drawdown | 0.8190 |
| cagr | -0.4789 |
| net_avg_win | 58.7987 |
| net_avg_loss | -75.1615 |
| avg_hold_time_bars | 14.0589 |
| exposure | 0.4774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
