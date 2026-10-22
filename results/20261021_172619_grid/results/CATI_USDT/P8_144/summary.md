# EMA Hourly Continuation — CATI/USDT P8_144

**Symbol:** CATI/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 236 |
| net_profit_factor | 0.6195 |
| net_win_rate | 0.4237 |
| gross_profit_factor | 0.7510 |
| gross_win_rate | 0.4237 |
| sharpe_ratio | -2.7417 |
| sortino_ratio | -0.6516 |
| max_drawdown | 0.5532 |
| cagr | -0.2623 |
| net_avg_win | 76.4006 |
| net_avg_loss | -90.6788 |
| avg_hold_time_bars | 59.2627 |
| exposure | 0.7667 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
