# EMA Hourly Continuation — GLM/USDT P55_144

**Symbol:** GLM/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.5715 |
| net_win_rate | 0.4742 |
| gross_profit_factor | 0.9267 |
| gross_win_rate | 0.4876 |
| sharpe_ratio | -3.7544 |
| sortino_ratio | -1.2096 |
| max_drawdown | 0.7691 |
| cagr | -0.4389 |
| net_avg_win | 41.1870 |
| net_avg_loss | -64.9882 |
| avg_hold_time_bars | 10.0841 |
| exposure | 0.2397 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
