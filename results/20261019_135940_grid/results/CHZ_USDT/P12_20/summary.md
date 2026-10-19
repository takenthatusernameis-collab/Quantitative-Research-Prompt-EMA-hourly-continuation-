# EMA Hourly Continuation — CHZ/USDT P12_20

**Symbol:** CHZ/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1535 |
| net_profit_factor | 0.3251 |
| net_win_rate | 0.3974 |
| gross_profit_factor | 0.8770 |
| gross_win_rate | 0.4293 |
| sharpe_ratio | -14.4207 |
| sortino_ratio | -8.0807 |
| max_drawdown | 1.0000 |
| cagr | -0.9854 |
| net_avg_win | 7.8965 |
| net_avg_loss | -16.0179 |
| avg_hold_time_bars | 2.2658 |
| exposure | 0.1581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
