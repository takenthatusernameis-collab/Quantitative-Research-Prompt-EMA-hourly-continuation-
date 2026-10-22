# EMA Hourly Continuation — FLUX/USDT P34_100

**Symbol:** FLUX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.7217 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9205 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -2.1778 |
| sortino_ratio | -0.6685 |
| max_drawdown | 0.5592 |
| cagr | -0.2646 |
| net_avg_win | 62.8427 |
| net_avg_loss | -80.5404 |
| avg_hold_time_bars | 10.7403 |
| exposure | 0.2255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
