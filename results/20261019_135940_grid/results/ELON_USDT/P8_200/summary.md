# EMA Hourly Continuation — ELON/USDT P8_200

**Symbol:** ELON/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.6259 |
| net_win_rate | 0.4641 |
| gross_profit_factor | 0.8696 |
| gross_win_rate | 0.4664 |
| sharpe_ratio | -3.0697 |
| sortino_ratio | -0.9152 |
| max_drawdown | 0.6646 |
| cagr | -0.3473 |
| net_avg_win | 53.1461 |
| net_avg_loss | -73.5384 |
| avg_hold_time_bars | 38.5493 |
| exposure | 0.7815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
