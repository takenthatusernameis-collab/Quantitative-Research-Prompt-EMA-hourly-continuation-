# EMA Hourly Continuation — SHR/USDT P8_200

**Symbol:** SHR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 833 |
| net_profit_factor | 0.4695 |
| net_win_rate | 0.3457 |
| gross_profit_factor | 0.6004 |
| gross_win_rate | 0.3457 |
| sharpe_ratio | -7.8143 |
| sortino_ratio | -3.1318 |
| max_drawdown | 0.9779 |
| cagr | -0.7769 |
| net_avg_win | 30.0284 |
| net_avg_loss | -33.7999 |
| avg_hold_time_bars | 17.3073 |
| exposure | 0.6524 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
