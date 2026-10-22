# EMA Hourly Continuation — XLM/USDT P20_50

**Symbol:** XLM/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1030 |
| net_profit_factor | 0.3024 |
| net_win_rate | 0.4379 |
| gross_profit_factor | 0.8425 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -9.0292 |
| sortino_ratio | -4.0720 |
| max_drawdown | 0.9944 |
| cagr | -0.8733 |
| net_avg_win | 9.5599 |
| net_avg_loss | -24.6213 |
| avg_hold_time_bars | 4.7456 |
| exposure | 0.2222 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
