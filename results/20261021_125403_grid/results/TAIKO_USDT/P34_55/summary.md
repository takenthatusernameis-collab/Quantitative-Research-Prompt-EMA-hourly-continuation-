# EMA Hourly Continuation — TAIKO/USDT P34_55

**Symbol:** TAIKO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.6739 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 0.9831 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -2.2276 |
| sortino_ratio | -0.5746 |
| max_drawdown | 0.5180 |
| cagr | -0.2305 |
| net_avg_win | 63.0198 |
| net_avg_loss | -92.8969 |
| avg_hold_time_bars | 6.3869 |
| exposure | 0.0936 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
