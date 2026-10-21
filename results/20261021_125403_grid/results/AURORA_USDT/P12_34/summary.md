# EMA Hourly Continuation — AURORA/USDT P12_34

**Symbol:** AURORA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.5844 |
| net_win_rate | 0.4481 |
| gross_profit_factor | 0.8574 |
| gross_win_rate | 0.4481 |
| sharpe_ratio | -4.4693 |
| sortino_ratio | -1.4809 |
| max_drawdown | 0.8339 |
| cagr | -0.4990 |
| net_avg_win | 47.8545 |
| net_avg_loss | -66.5020 |
| avg_hold_time_bars | 8.8056 |
| exposure | 0.2161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
