# EMA Hourly Continuation — GLM/USDT P50_144

**Symbol:** GLM/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.5827 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.9272 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -3.7379 |
| sortino_ratio | -1.2049 |
| max_drawdown | 0.7655 |
| cagr | -0.4353 |
| net_avg_win | 43.2509 |
| net_avg_loss | -66.6390 |
| avg_hold_time_bars | 11.5231 |
| exposure | 0.2724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
