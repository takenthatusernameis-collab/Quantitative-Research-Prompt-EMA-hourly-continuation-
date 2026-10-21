# EMA Hourly Continuation — CVX/USDT P50_100

**Symbol:** CVX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.8921 |
| net_win_rate | 0.5370 |
| gross_profit_factor | 1.1587 |
| gross_win_rate | 0.5370 |
| sharpe_ratio | -0.6920 |
| sortino_ratio | -0.1912 |
| max_drawdown | 0.2843 |
| cagr | -0.0867 |
| net_avg_win | 85.8713 |
| net_avg_loss | -111.6370 |
| avg_hold_time_bars | 9.4767 |
| exposure | 0.1572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
