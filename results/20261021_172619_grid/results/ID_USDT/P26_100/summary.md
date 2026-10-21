# EMA Hourly Continuation — ID/USDT P26_100

**Symbol:** ID/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.7892 |
| net_win_rate | 0.5030 |
| gross_profit_factor | 1.0108 |
| gross_win_rate | 0.5030 |
| sharpe_ratio | -1.6340 |
| sortino_ratio | -0.5200 |
| max_drawdown | 0.4807 |
| cagr | -0.2129 |
| net_avg_win | 68.1499 |
| net_avg_loss | -87.4071 |
| avg_hold_time_bars | 16.3980 |
| exposure | 0.3673 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
