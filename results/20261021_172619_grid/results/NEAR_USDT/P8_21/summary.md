# EMA Hourly Continuation — NEAR/USDT P8_21

**Symbol:** NEAR/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.8171 |
| net_win_rate | 0.5148 |
| gross_profit_factor | 1.0830 |
| gross_win_rate | 0.5148 |
| sharpe_ratio | -1.5383 |
| sortino_ratio | -0.4821 |
| max_drawdown | 0.4912 |
| cagr | -0.1992 |
| net_avg_win | 78.2879 |
| net_avg_loss | -101.6404 |
| avg_hold_time_bars | 5.6287 |
| exposure | 0.1213 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
