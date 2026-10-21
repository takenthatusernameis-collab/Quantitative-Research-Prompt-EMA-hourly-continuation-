# EMA Hourly Continuation — ATOM/USDT P8_12

**Symbol:** ATOM/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 182 |
| net_profit_factor | 0.6450 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 0.9483 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -1.7779 |
| sortino_ratio | -0.3449 |
| max_drawdown | 0.3271 |
| cagr | -0.1459 |
| net_avg_win | 66.7612 |
| net_avg_loss | -99.0587 |
| avg_hold_time_bars | 4.5989 |
| exposure | 0.0380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
