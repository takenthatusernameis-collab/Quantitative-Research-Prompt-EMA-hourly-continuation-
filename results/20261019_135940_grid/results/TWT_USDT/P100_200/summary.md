# EMA Hourly Continuation — TWT/USDT P100_200

**Symbol:** TWT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.4537 |
| net_win_rate | 0.4436 |
| gross_profit_factor | 0.8006 |
| gross_win_rate | 0.4485 |
| sharpe_ratio | -4.6652 |
| sortino_ratio | -1.3305 |
| max_drawdown | 0.8104 |
| cagr | -0.4745 |
| net_avg_win | 36.7600 |
| net_avg_loss | -64.6072 |
| avg_hold_time_bars | 9.5049 |
| exposure | 0.1763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
