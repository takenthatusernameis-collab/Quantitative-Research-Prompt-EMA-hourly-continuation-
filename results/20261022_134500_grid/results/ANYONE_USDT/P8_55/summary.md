# EMA Hourly Continuation — ANYONE/USDT P8_55

**Symbol:** ANYONE/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 949 |
| net_profit_factor | 0.7013 |
| net_win_rate | 0.4679 |
| gross_profit_factor | 0.9148 |
| gross_win_rate | 0.4689 |
| sharpe_ratio | -4.1178 |
| sortino_ratio | -1.8872 |
| max_drawdown | 0.8717 |
| cagr | -0.5885 |
| net_avg_win | 45.7770 |
| net_avg_loss | -57.3859 |
| avg_hold_time_bars | 9.9083 |
| exposure | 0.4751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
