# EMA Hourly Continuation — RAY/USDT P20_34

**Symbol:** RAY/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.7593 |
| net_win_rate | 0.5028 |
| gross_profit_factor | 1.0443 |
| gross_win_rate | 0.5085 |
| sharpe_ratio | -1.7184 |
| sortino_ratio | -0.4626 |
| max_drawdown | 0.4364 |
| cagr | -0.1921 |
| net_avg_win | 73.9348 |
| net_avg_loss | -98.4820 |
| avg_hold_time_bars | 5.3722 |
| exposure | 0.0860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
