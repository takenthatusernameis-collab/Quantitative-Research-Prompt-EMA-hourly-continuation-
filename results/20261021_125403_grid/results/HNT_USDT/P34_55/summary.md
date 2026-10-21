# EMA Hourly Continuation — HNT/USDT P34_55

**Symbol:** HNT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.8445 |
| net_win_rate | 0.5329 |
| gross_profit_factor | 1.1189 |
| gross_win_rate | 0.5329 |
| sharpe_ratio | -0.8084 |
| sortino_ratio | -0.1986 |
| max_drawdown | 0.2409 |
| cagr | -0.0885 |
| net_avg_win | 73.1836 |
| net_avg_loss | -98.8550 |
| avg_hold_time_bars | 6.3806 |
| exposure | 0.0838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
