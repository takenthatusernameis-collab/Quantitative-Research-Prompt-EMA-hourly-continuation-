# EMA Hourly Continuation — POKT/USDT P34_100

**Symbol:** POKT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.7042 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 0.9081 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -2.6911 |
| sortino_ratio | -0.8309 |
| max_drawdown | 0.6407 |
| cagr | -0.3189 |
| net_avg_win | 66.8352 |
| net_avg_loss | -82.2563 |
| avg_hold_time_bars | 13.2185 |
| exposure | 0.2847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
