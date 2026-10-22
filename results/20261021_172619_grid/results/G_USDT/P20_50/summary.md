# EMA Hourly Continuation — G/USDT P20_50

**Symbol:** G/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.5732 |
| net_win_rate | 0.4505 |
| gross_profit_factor | 0.8213 |
| gross_win_rate | 0.4505 |
| sharpe_ratio | -4.3221 |
| sortino_ratio | -1.5346 |
| max_drawdown | 0.8027 |
| cagr | -0.5056 |
| net_avg_win | 43.6557 |
| net_avg_loss | -62.4275 |
| avg_hold_time_bars | 9.0953 |
| exposure | 0.2559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
