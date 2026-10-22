# EMA Hourly Continuation — SATS/USDT P20_21

**Symbol:** SATS/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 151 |
| net_profit_factor | 0.7029 |
| net_win_rate | 0.4967 |
| gross_profit_factor | 0.9905 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -1.3560 |
| sortino_ratio | -0.2379 |
| max_drawdown | 0.2753 |
| cagr | -0.1040 |
| net_avg_win | 76.3489 |
| net_avg_loss | -107.1865 |
| avg_hold_time_bars | 4.8742 |
| exposure | 0.0333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
