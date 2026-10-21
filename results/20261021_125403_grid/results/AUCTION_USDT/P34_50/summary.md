# EMA Hourly Continuation — AUCTION/USDT P34_50

**Symbol:** AUCTION/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.5538 |
| net_win_rate | 0.4599 |
| gross_profit_factor | 0.8798 |
| gross_win_rate | 0.4599 |
| sharpe_ratio | -4.0905 |
| sortino_ratio | -1.1854 |
| max_drawdown | 0.7550 |
| cagr | -0.4239 |
| net_avg_win | 49.3298 |
| net_avg_loss | -75.8340 |
| avg_hold_time_bars | 5.8662 |
| exposure | 0.1091 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
