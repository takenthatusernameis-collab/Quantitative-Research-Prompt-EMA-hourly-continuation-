# EMA Hourly Continuation — GMX/USDT P21_144

**Symbol:** GMX/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 598 |
| net_profit_factor | 0.6347 |
| net_win_rate | 0.4582 |
| gross_profit_factor | 0.8920 |
| gross_win_rate | 0.4632 |
| sharpe_ratio | -3.6648 |
| sortino_ratio | -1.2658 |
| max_drawdown | 0.7857 |
| cagr | -0.4473 |
| net_avg_win | 49.1061 |
| net_avg_loss | -65.4297 |
| avg_hold_time_bars | 18.0953 |
| exposure | 0.4919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
