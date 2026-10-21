# EMA Hourly Continuation — GLM/USDT P20_34

**Symbol:** GLM/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.5687 |
| net_win_rate | 0.4496 |
| gross_profit_factor | 0.8967 |
| gross_win_rate | 0.4496 |
| sharpe_ratio | -4.6884 |
| sortino_ratio | -1.4956 |
| max_drawdown | 0.8385 |
| cagr | -0.4999 |
| net_avg_win | 48.7501 |
| net_avg_loss | -70.0234 |
| avg_hold_time_bars | 5.7077 |
| exposure | 0.1287 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
