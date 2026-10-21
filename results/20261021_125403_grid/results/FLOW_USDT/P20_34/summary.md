# EMA Hourly Continuation — FLOW/USDT P20_34

**Symbol:** FLOW/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.5198 |
| net_win_rate | 0.4355 |
| gross_profit_factor | 0.7848 |
| gross_win_rate | 0.4355 |
| sharpe_ratio | -3.8891 |
| sortino_ratio | -1.0725 |
| max_drawdown | 0.7200 |
| cagr | -0.3892 |
| net_avg_win | 47.4361 |
| net_avg_loss | -70.4030 |
| avg_hold_time_bars | 5.3172 |
| exposure | 0.0899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
