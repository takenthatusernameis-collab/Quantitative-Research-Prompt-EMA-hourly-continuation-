# EMA Hourly Continuation — FIDA/USDT P20_34

**Symbol:** FIDA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1105 |
| net_profit_factor | 0.4391 |
| net_win_rate | 0.4253 |
| gross_profit_factor | 0.9165 |
| gross_win_rate | 0.4543 |
| sharpe_ratio | -9.2029 |
| sortino_ratio | -4.3298 |
| max_drawdown | 0.9955 |
| cagr | -0.8819 |
| net_avg_win | 16.5799 |
| net_avg_loss | -27.9478 |
| avg_hold_time_bars | 3.4471 |
| exposure | 0.1724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
