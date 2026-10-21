# EMA Hourly Continuation — YGG/USDT P12_200

**Symbol:** YGG/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.8172 |
| net_win_rate | 0.4859 |
| gross_profit_factor | 0.9554 |
| gross_win_rate | 0.4859 |
| sharpe_ratio | -1.2693 |
| sortino_ratio | -0.3397 |
| max_drawdown | 0.4033 |
| cagr | -0.1464 |
| net_avg_win | 85.5339 |
| net_avg_loss | -98.9186 |
| avg_hold_time_bars | 43.6751 |
| exposure | 0.6996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
