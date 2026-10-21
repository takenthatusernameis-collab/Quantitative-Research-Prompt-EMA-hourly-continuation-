# EMA Hourly Continuation — SEI/USDT P8_21

**Symbol:** SEI/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.7505 |
| net_win_rate | 0.4961 |
| gross_profit_factor | 1.0005 |
| gross_win_rate | 0.4961 |
| sharpe_ratio | -2.2495 |
| sortino_ratio | -0.7328 |
| max_drawdown | 0.6061 |
| cagr | -0.2854 |
| net_avg_win | 66.9533 |
| net_avg_loss | -87.8448 |
| avg_hold_time_bars | 6.0969 |
| exposure | 0.1430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
