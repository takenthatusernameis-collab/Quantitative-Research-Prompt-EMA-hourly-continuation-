# EMA Hourly Continuation — YFI/USDT P55_100

**Symbol:** YFI/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.5879 |
| net_win_rate | 0.4707 |
| gross_profit_factor | 0.9126 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -3.5495 |
| sortino_ratio | -1.0497 |
| max_drawdown | 0.7218 |
| cagr | -0.3832 |
| net_avg_win | 50.0037 |
| net_avg_loss | -75.6419 |
| avg_hold_time_bars | 7.8197 |
| exposure | 0.1511 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
