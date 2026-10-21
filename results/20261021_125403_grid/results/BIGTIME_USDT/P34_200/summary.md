# EMA Hourly Continuation — BIGTIME/USDT P34_200

**Symbol:** BIGTIME/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.9825 |
| net_win_rate | 0.5406 |
| gross_profit_factor | 1.1719 |
| gross_win_rate | 0.5406 |
| sharpe_ratio | -0.0421 |
| sortino_ratio | -0.0102 |
| max_drawdown | 0.1712 |
| cagr | -0.0100 |
| net_avg_win | 91.5582 |
| net_avg_loss | -109.6757 |
| avg_hold_time_bars | 43.3145 |
| exposure | 0.5547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
