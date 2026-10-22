# EMA Hourly Continuation — FET/USDT P12_50

**Symbol:** FET/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1099 |
| net_profit_factor | 0.5693 |
| net_win_rate | 0.4695 |
| gross_profit_factor | 0.8819 |
| gross_win_rate | 0.4732 |
| sharpe_ratio | -6.0098 |
| sortino_ratio | -2.7939 |
| max_drawdown | 0.9676 |
| cagr | -0.7427 |
| net_avg_win | 24.7667 |
| net_avg_loss | -38.5058 |
| avg_hold_time_bars | 6.7598 |
| exposure | 0.3377 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
