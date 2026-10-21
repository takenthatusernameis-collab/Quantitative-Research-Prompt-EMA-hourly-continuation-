# EMA Hourly Continuation — CRO/USDT P34_144

**Symbol:** CRO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.7894 |
| net_win_rate | 0.5246 |
| gross_profit_factor | 1.0786 |
| gross_win_rate | 0.5246 |
| sharpe_ratio | -1.2598 |
| sortino_ratio | -0.3368 |
| max_drawdown | 0.3797 |
| cagr | -0.1441 |
| net_avg_win | 66.9755 |
| net_avg_loss | -93.6433 |
| avg_hold_time_bars | 25.9536 |
| exposure | 0.4070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
