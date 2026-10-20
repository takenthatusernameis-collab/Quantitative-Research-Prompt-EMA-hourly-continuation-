# EMA Hourly Continuation — GLM/USDT P89_200

**Symbol:** GLM/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.5523 |
| net_win_rate | 0.4624 |
| gross_profit_factor | 0.9094 |
| gross_win_rate | 0.4742 |
| sharpe_ratio | -3.8413 |
| sortino_ratio | -1.1178 |
| max_drawdown | 0.7487 |
| cagr | -0.4167 |
| net_avg_win | 46.4502 |
| net_avg_loss | -72.3510 |
| avg_hold_time_bars | 11.0869 |
| exposure | 0.2147 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
