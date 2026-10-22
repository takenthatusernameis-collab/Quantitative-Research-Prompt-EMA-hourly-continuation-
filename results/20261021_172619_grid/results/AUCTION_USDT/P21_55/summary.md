# EMA Hourly Continuation — AUCTION/USDT P21_55

**Symbol:** AUCTION/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.5781 |
| net_win_rate | 0.4535 |
| gross_profit_factor | 0.8290 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -4.5445 |
| sortino_ratio | -1.5936 |
| max_drawdown | 0.8536 |
| cagr | -0.5253 |
| net_avg_win | 41.7651 |
| net_avg_loss | -59.9497 |
| avg_hold_time_bars | 8.6786 |
| exposure | 0.2408 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
