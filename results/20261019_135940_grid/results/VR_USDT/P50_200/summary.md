# EMA Hourly Continuation — VR/USDT P50_200

**Symbol:** VR/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.4384 |
| net_win_rate | 0.3180 |
| gross_profit_factor | 0.6354 |
| gross_win_rate | 0.3240 |
| sharpe_ratio | -8.7667 |
| sortino_ratio | -2.7355 |
| max_drawdown | 0.9802 |
| cagr | -0.7883 |
| net_avg_win | 48.1102 |
| net_avg_loss | -51.1638 |
| avg_hold_time_bars | 15.8720 |
| exposure | 0.3607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
