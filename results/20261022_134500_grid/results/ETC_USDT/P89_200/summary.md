# EMA Hourly Continuation — ETC/USDT P89_200

**Symbol:** ETC/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.5012 |
| net_win_rate | 0.4386 |
| gross_profit_factor | 0.8671 |
| gross_win_rate | 0.4530 |
| sharpe_ratio | -4.8317 |
| sortino_ratio | -1.3962 |
| max_drawdown | 0.8227 |
| cagr | -0.4903 |
| net_avg_win | 45.0513 |
| net_avg_loss | -70.2107 |
| avg_hold_time_bars | 9.9133 |
| exposure | 0.1870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
