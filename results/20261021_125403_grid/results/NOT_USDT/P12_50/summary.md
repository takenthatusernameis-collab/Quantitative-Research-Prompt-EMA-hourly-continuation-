# EMA Hourly Continuation — NOT/USDT P12_50

**Symbol:** NOT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 564 |
| net_profit_factor | 0.7941 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9845 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.6837 |
| sortino_ratio | -0.5824 |
| max_drawdown | 0.5181 |
| cagr | -0.2358 |
| net_avg_win | 65.6352 |
| net_avg_loss | -82.6488 |
| avg_hold_time_bars | 11.7801 |
| exposure | 0.3121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
