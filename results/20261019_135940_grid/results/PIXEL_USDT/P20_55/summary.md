# EMA Hourly Continuation — PIXEL/USDT P20_55

**Symbol:** PIXEL/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 923 |
| net_profit_factor | 0.5707 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.9067 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -5.4274 |
| sortino_ratio | -2.3264 |
| max_drawdown | 0.9414 |
| cagr | -0.6702 |
| net_avg_win | 29.3066 |
| net_avg_loss | -44.0150 |
| avg_hold_time_bars | 6.6522 |
| exposure | 0.2778 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
