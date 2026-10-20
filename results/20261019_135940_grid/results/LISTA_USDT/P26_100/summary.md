# EMA Hourly Continuation — LISTA/USDT P26_100

**Symbol:** LISTA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 591 |
| net_profit_factor | 0.6390 |
| net_win_rate | 0.4670 |
| gross_profit_factor | 0.9193 |
| gross_win_rate | 0.4772 |
| sharpe_ratio | -3.6791 |
| sortino_ratio | -1.3031 |
| max_drawdown | 0.7662 |
| cagr | -0.4613 |
| net_avg_win | 49.0072 |
| net_avg_loss | -67.1933 |
| avg_hold_time_bars | 12.2369 |
| exposure | 0.3536 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
