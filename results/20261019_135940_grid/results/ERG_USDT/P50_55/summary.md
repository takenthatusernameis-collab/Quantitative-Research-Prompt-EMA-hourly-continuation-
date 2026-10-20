# EMA Hourly Continuation — ERG/USDT P50_55

**Symbol:** ERG/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 832 |
| net_profit_factor | 0.0595 |
| net_win_rate | 0.2296 |
| gross_profit_factor | 0.2320 |
| gross_win_rate | 0.2933 |
| sharpe_ratio | -15.8959 |
| sortino_ratio | -7.0364 |
| max_drawdown | 0.9999 |
| cagr | -0.9799 |
| net_avg_win | 3.3098 |
| net_avg_loss | -16.5860 |
| avg_hold_time_bars | 2.7332 |
| exposure | 0.1034 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
