# EMA Hourly Continuation — GALA/USDT P8_50

**Symbol:** GALA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.7584 |
| net_win_rate | 0.4869 |
| gross_profit_factor | 0.9394 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -2.2305 |
| sortino_ratio | -0.8359 |
| max_drawdown | 0.6388 |
| cagr | -0.3196 |
| net_avg_win | 58.0752 |
| net_avg_loss | -72.6726 |
| avg_hold_time_bars | 13.4390 |
| exposure | 0.4203 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
