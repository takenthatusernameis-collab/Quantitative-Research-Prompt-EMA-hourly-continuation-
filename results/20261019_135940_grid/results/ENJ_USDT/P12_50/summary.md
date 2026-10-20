# EMA Hourly Continuation — ENJ/USDT P12_50

**Symbol:** ENJ/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1077 |
| net_profit_factor | 0.5240 |
| net_win_rate | 0.4624 |
| gross_profit_factor | 0.9238 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -6.8918 |
| sortino_ratio | -3.1609 |
| max_drawdown | 0.9810 |
| cagr | -0.7920 |
| net_avg_win | 21.6810 |
| net_avg_loss | -35.5844 |
| avg_hold_time_bars | 6.6778 |
| exposure | 0.3269 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
