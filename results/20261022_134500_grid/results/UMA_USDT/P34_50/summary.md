# EMA Hourly Continuation — UMA/USDT P34_50

**Symbol:** UMA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 908 |
| net_profit_factor | 0.3750 |
| net_win_rate | 0.4218 |
| gross_profit_factor | 0.8429 |
| gross_win_rate | 0.4504 |
| sharpe_ratio | -9.1757 |
| sortino_ratio | -3.9429 |
| max_drawdown | 0.9931 |
| cagr | -0.8599 |
| net_avg_win | 15.5522 |
| net_avg_loss | -30.2565 |
| avg_hold_time_bars | 3.5066 |
| exposure | 0.1447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
