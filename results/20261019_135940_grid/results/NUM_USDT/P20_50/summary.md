# EMA Hourly Continuation — NUM/USDT P20_50

**Symbol:** NUM/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 980 |
| net_profit_factor | 0.3660 |
| net_win_rate | 0.3551 |
| gross_profit_factor | 0.7350 |
| gross_win_rate | 0.3714 |
| sharpe_ratio | -10.6356 |
| sortino_ratio | -4.6981 |
| max_drawdown | 0.9974 |
| cagr | -0.9059 |
| net_avg_win | 16.5433 |
| net_avg_loss | -24.8903 |
| avg_hold_time_bars | 5.3908 |
| exposure | 0.2401 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
