# EMA Hourly Continuation — NEAR/USDT P20_21

**Symbol:** NEAR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1210 |
| net_profit_factor | 0.1692 |
| net_win_rate | 0.2909 |
| gross_profit_factor | 0.6417 |
| gross_win_rate | 0.3388 |
| sharpe_ratio | -18.1127 |
| sortino_ratio | -9.5729 |
| max_drawdown | 1.0000 |
| cagr | -0.9961 |
| net_avg_win | 5.7877 |
| net_avg_loss | -14.0294 |
| avg_hold_time_bars | 1.5702 |
| exposure | 0.0864 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
