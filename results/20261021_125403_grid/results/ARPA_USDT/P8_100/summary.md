# EMA Hourly Continuation — ARPA/USDT P8_100

**Symbol:** ARPA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 616 |
| net_profit_factor | 0.6837 |
| net_win_rate | 0.4756 |
| gross_profit_factor | 0.8836 |
| gross_win_rate | 0.4756 |
| sharpe_ratio | -2.8513 |
| sortino_ratio | -1.0062 |
| max_drawdown | 0.6970 |
| cagr | -0.3698 |
| net_avg_win | 50.7606 |
| net_avg_loss | -67.3470 |
| avg_hold_time_bars | 21.4643 |
| exposure | 0.5983 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
