# EMA Hourly Continuation — IOTX/USDT P12_21

**Symbol:** IOTX/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.7774 |
| net_win_rate | 0.5344 |
| gross_profit_factor | 1.1404 |
| gross_win_rate | 0.5344 |
| sharpe_ratio | -1.4620 |
| sortino_ratio | -0.4034 |
| max_drawdown | 0.3796 |
| cagr | -0.1680 |
| net_avg_win | 66.6077 |
| net_avg_loss | -98.3536 |
| avg_hold_time_bars | 5.1212 |
| exposure | 0.0845 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
