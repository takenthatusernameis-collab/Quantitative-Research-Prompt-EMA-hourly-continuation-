# EMA Hourly Continuation — YGG/USDT P20_50

**Symbol:** YGG/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1005 |
| net_profit_factor | 0.5583 |
| net_win_rate | 0.4507 |
| gross_profit_factor | 0.8945 |
| gross_win_rate | 0.4637 |
| sharpe_ratio | -6.6912 |
| sortino_ratio | -2.9763 |
| max_drawdown | 0.9739 |
| cagr | -0.7633 |
| net_avg_win | 27.1715 |
| net_avg_loss | -39.9364 |
| avg_hold_time_bars | 4.8000 |
| exposure | 0.2183 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
