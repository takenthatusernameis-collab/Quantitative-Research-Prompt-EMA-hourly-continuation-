# EMA Hourly Continuation — GLM/USDT P8_144

**Symbol:** GLM/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 558 |
| net_profit_factor | 0.5939 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.8890 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -4.0713 |
| sortino_ratio | -1.3426 |
| max_drawdown | 0.8121 |
| cagr | -0.4790 |
| net_avg_win | 45.8439 |
| net_avg_loss | -65.9021 |
| avg_hold_time_bars | 27.8710 |
| exposure | 0.7069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
