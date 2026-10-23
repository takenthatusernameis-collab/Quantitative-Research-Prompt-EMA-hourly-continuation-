# EMA Hourly Continuation — WIN/USDT P12_100

**Symbol:** WIN/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 606 |
| net_profit_factor | 0.4793 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 0.8509 |
| gross_win_rate | 0.4736 |
| sharpe_ratio | -5.0285 |
| sortino_ratio | -1.7258 |
| max_drawdown | 0.8897 |
| cagr | -0.5808 |
| net_avg_win | 29.1729 |
| net_avg_loss | -52.2763 |
| avg_hold_time_bars | 21.6799 |
| exposure | 0.5972 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
