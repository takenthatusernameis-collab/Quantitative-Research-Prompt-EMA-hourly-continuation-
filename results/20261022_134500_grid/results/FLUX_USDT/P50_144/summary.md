# EMA Hourly Continuation — FLUX/USDT P50_144

**Symbol:** FLUX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.6686 |
| net_win_rate | 0.5063 |
| gross_profit_factor | 1.0176 |
| gross_win_rate | 0.5146 |
| sharpe_ratio | -2.4743 |
| sortino_ratio | -0.7675 |
| max_drawdown | 0.6048 |
| cagr | -0.3051 |
| net_avg_win | 49.9547 |
| net_avg_loss | -76.6125 |
| avg_hold_time_bars | 14.3201 |
| exposure | 0.3111 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
