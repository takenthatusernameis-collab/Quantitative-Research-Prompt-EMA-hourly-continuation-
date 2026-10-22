# EMA Hourly Continuation — TNSR/USDT P100_200

**Symbol:** TNSR/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.7706 |
| net_win_rate | 0.4947 |
| gross_profit_factor | 0.9624 |
| gross_win_rate | 0.4947 |
| sharpe_ratio | -1.3164 |
| sortino_ratio | -0.3172 |
| max_drawdown | 0.3305 |
| cagr | -0.1361 |
| net_avg_win | 73.5060 |
| net_avg_loss | -93.4036 |
| avg_hold_time_bars | 15.0632 |
| exposure | 0.1943 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
