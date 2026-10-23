# EMA Hourly Continuation — LSK/USDT P8_20

**Symbol:** LSK/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1282 |
| net_profit_factor | 0.4553 |
| net_win_rate | 0.4477 |
| gross_profit_factor | 1.0137 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -9.3363 |
| sortino_ratio | -4.7186 |
| max_drawdown | 0.9974 |
| cagr | -0.9044 |
| net_avg_win | 14.5227 |
| net_avg_loss | -25.8595 |
| avg_hold_time_bars | 4.2231 |
| exposure | 0.2461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
