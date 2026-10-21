# EMA Hourly Continuation — TRB/USDT P50_100

**Symbol:** TRB/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.6651 |
| net_win_rate | 0.4693 |
| gross_profit_factor | 0.8858 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -2.4592 |
| sortino_ratio | -0.6623 |
| max_drawdown | 0.5555 |
| cagr | -0.2608 |
| net_avg_win | 63.0554 |
| net_avg_loss | -83.8315 |
| avg_hold_time_bars | 10.1564 |
| exposure | 0.1645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
