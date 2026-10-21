# EMA Hourly Continuation — MEW/USDT P26_100

**Symbol:** MEW/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.6914 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.8440 |
| gross_win_rate | 0.4661 |
| sharpe_ratio | -2.3174 |
| sortino_ratio | -0.7044 |
| max_drawdown | 0.5794 |
| cagr | -0.2763 |
| net_avg_win | 58.4746 |
| net_avg_loss | -73.8331 |
| avg_hold_time_bars | 14.8446 |
| exposure | 0.3084 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
