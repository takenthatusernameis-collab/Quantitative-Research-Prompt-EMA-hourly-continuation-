# EMA Hourly Continuation — IOTA/USDT P8_12

**Symbol:** IOTA/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1907 |
| net_profit_factor | 0.1287 |
| net_win_rate | 0.3744 |
| gross_profit_factor | 0.6074 |
| gross_win_rate | 0.4263 |
| sharpe_ratio | -17.9872 |
| sortino_ratio | -11.4230 |
| max_drawdown | 1.0000 |
| cagr | -0.9975 |
| net_avg_win | 2.0691 |
| net_avg_loss | -9.6206 |
| avg_hold_time_bars | 1.9250 |
| exposure | 0.1669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
