# EMA Hourly Continuation — POPCAT/USDT P55_100

**Symbol:** POPCAT/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.5616 |
| net_win_rate | 0.4431 |
| gross_profit_factor | 0.8113 |
| gross_win_rate | 0.4499 |
| sharpe_ratio | -4.9618 |
| sortino_ratio | -1.8327 |
| max_drawdown | 0.8499 |
| cagr | -0.5817 |
| net_avg_win | 41.6072 |
| net_avg_loss | -58.9584 |
| avg_hold_time_bars | 5.6129 |
| exposure | 0.1746 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
