# EMA Hourly Continuation — ARB/USDT P34_50

**Symbol:** ARB/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 884 |
| net_profit_factor | 0.3713 |
| net_win_rate | 0.4400 |
| gross_profit_factor | 0.8865 |
| gross_win_rate | 0.4570 |
| sharpe_ratio | -8.4677 |
| sortino_ratio | -3.5647 |
| max_drawdown | 0.9894 |
| cagr | -0.8361 |
| net_avg_win | 15.0210 |
| net_avg_loss | -31.7912 |
| avg_hold_time_bars | 2.8043 |
| exposure | 0.1127 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
