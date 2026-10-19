# EMA Hourly Continuation — CRV/USDT P20_55

**Symbol:** CRV/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 955 |
| net_profit_factor | 0.6214 |
| net_win_rate | 0.4838 |
| gross_profit_factor | 1.0383 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -5.4353 |
| sortino_ratio | -2.3607 |
| max_drawdown | 0.9455 |
| cagr | -0.6833 |
| net_avg_win | 33.5508 |
| net_avg_loss | -50.5948 |
| avg_hold_time_bars | 4.9319 |
| exposure | 0.2141 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
