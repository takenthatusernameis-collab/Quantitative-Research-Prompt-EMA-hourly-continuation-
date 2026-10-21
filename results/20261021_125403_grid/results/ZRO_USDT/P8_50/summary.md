# EMA Hourly Continuation — ZRO/USDT P8_50

**Symbol:** ZRO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 616 |
| net_profit_factor | 0.9129 |
| net_win_rate | 0.5260 |
| gross_profit_factor | 1.0996 |
| gross_win_rate | 0.5260 |
| sharpe_ratio | -0.6792 |
| sortino_ratio | -0.2522 |
| max_drawdown | 0.3308 |
| cagr | -0.1164 |
| net_avg_win | 81.0665 |
| net_avg_loss | -98.5342 |
| avg_hold_time_bars | 14.1802 |
| exposure | 0.4275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
