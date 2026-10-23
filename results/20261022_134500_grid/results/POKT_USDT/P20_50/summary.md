# EMA Hourly Continuation — POKT/USDT P20_50

**Symbol:** POKT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1127 |
| net_profit_factor | 0.4739 |
| net_win_rate | 0.4011 |
| gross_profit_factor | 0.8675 |
| gross_win_rate | 0.4126 |
| sharpe_ratio | -9.4022 |
| sortino_ratio | -4.4177 |
| max_drawdown | 0.9961 |
| cagr | -0.8885 |
| net_avg_win | 19.8468 |
| net_avg_loss | -28.0463 |
| avg_hold_time_bars | 4.9246 |
| exposure | 0.2512 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
