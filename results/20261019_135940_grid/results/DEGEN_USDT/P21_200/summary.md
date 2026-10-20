# EMA Hourly Continuation — DEGEN/USDT P21_200

**Symbol:** DEGEN/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.7212 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.9427 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -2.1969 |
| sortino_ratio | -0.6228 |
| max_drawdown | 0.5415 |
| cagr | -0.2577 |
| net_avg_win | 70.5415 |
| net_avg_loss | -88.6262 |
| avg_hold_time_bars | 33.9384 |
| exposure | 0.6273 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
