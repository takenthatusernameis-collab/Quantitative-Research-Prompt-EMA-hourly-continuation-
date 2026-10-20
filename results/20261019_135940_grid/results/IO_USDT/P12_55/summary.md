# EMA Hourly Continuation — IO/USDT P12_55

**Symbol:** IO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 976 |
| net_profit_factor | 0.6376 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.9115 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -5.1885 |
| sortino_ratio | -2.3442 |
| max_drawdown | 0.9334 |
| cagr | -0.6771 |
| net_avg_win | 35.9040 |
| net_avg_loss | -49.3777 |
| avg_hold_time_bars | 7.9324 |
| exposure | 0.3748 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
