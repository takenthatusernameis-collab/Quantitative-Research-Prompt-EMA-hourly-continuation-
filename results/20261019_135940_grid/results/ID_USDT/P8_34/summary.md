# EMA Hourly Continuation — ID/USDT P8_34

**Symbol:** ID/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1225 |
| net_profit_factor | 0.5731 |
| net_win_rate | 0.4514 |
| gross_profit_factor | 1.0357 |
| gross_win_rate | 0.4710 |
| sharpe_ratio | -7.2940 |
| sortino_ratio | -3.5898 |
| max_drawdown | 0.9882 |
| cagr | -0.8226 |
| net_avg_win | 23.9642 |
| net_avg_loss | -34.4118 |
| avg_hold_time_bars | 6.4049 |
| exposure | 0.3551 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
