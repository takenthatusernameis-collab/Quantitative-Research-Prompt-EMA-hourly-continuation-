# EMA Hourly Continuation — PUNDIX/USDT P34_100

**Symbol:** PUNDIX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.6703 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9313 |
| gross_win_rate | 0.4835 |
| sharpe_ratio | -2.7645 |
| sortino_ratio | -0.8710 |
| max_drawdown | 0.6382 |
| cagr | -0.3290 |
| net_avg_win | 54.9727 |
| net_avg_loss | -76.1572 |
| avg_hold_time_bars | 12.6049 |
| exposure | 0.2785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
