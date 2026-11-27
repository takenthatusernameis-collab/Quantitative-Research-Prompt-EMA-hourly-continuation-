# EMA Hourly Continuation — SHR/USDT P34_144

**Symbol:** SHR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 752 |
| net_profit_factor | 0.4269 |
| net_win_rate | 0.3431 |
| gross_profit_factor | 0.5629 |
| gross_win_rate | 0.3444 |
| sharpe_ratio | -7.5255 |
| sortino_ratio | -2.8770 |
| max_drawdown | 0.9699 |
| cagr | -0.7468 |
| net_avg_win | 27.9708 |
| net_avg_loss | -34.2181 |
| avg_hold_time_bars | 10.0931 |
| exposure | 0.3435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
