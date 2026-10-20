# EMA Hourly Continuation — XEC/USDT P34_55

**Symbol:** XEC/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 962 |
| net_profit_factor | 0.3668 |
| net_win_rate | 0.4179 |
| gross_profit_factor | 0.8570 |
| gross_win_rate | 0.4470 |
| sharpe_ratio | -9.7608 |
| sortino_ratio | -4.3237 |
| max_drawdown | 0.9957 |
| cagr | -0.8843 |
| net_avg_win | 14.3505 |
| net_avg_loss | -28.0813 |
| avg_hold_time_bars | 3.6341 |
| exposure | 0.1582 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
