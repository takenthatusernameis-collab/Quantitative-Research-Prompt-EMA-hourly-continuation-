# EMA Hourly Continuation — TNSR/USDT P100_200

**Symbol:** TNSR/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.6167 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.8954 |
| gross_win_rate | 0.4794 |
| sharpe_ratio | -2.9347 |
| sortino_ratio | -0.8144 |
| max_drawdown | 0.6250 |
| cagr | -0.3197 |
| net_avg_win | 54.9382 |
| net_avg_loss | -78.7077 |
| avg_hold_time_bars | 11.5722 |
| exposure | 0.2032 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
