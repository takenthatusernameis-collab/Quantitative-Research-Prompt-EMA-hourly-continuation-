# EMA Hourly Continuation — GLM/USDT P20_89

**Symbol:** GLM/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 692 |
| net_profit_factor | 0.5321 |
| net_win_rate | 0.4480 |
| gross_profit_factor | 0.8368 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -5.0882 |
| sortino_ratio | -1.8854 |
| max_drawdown | 0.8980 |
| cagr | -0.5940 |
| net_avg_win | 32.8660 |
| net_avg_loss | -50.1271 |
| avg_hold_time_bars | 13.2327 |
| exposure | 0.4162 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
