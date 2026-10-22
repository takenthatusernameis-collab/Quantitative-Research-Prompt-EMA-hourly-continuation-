# EMA Hourly Continuation — CRV/USDT P100_144

**Symbol:** CRV/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 565 |
| net_profit_factor | 0.4162 |
| net_win_rate | 0.4319 |
| gross_profit_factor | 0.7414 |
| gross_win_rate | 0.4407 |
| sharpe_ratio | -6.0617 |
| sortino_ratio | -2.0325 |
| max_drawdown | 0.9214 |
| cagr | -0.6343 |
| net_avg_win | 26.8841 |
| net_avg_loss | -49.0962 |
| avg_hold_time_bars | 3.5735 |
| exposure | 0.0918 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
