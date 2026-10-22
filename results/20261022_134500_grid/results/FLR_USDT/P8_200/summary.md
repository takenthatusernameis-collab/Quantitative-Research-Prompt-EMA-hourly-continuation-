# EMA Hourly Continuation — FLR/USDT P8_200

**Symbol:** FLR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 622 |
| net_profit_factor | 0.5477 |
| net_win_rate | 0.4582 |
| gross_profit_factor | 0.8590 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -4.6677 |
| sortino_ratio | -1.6236 |
| max_drawdown | 0.8709 |
| cagr | -0.5498 |
| net_avg_win | 36.7671 |
| net_avg_loss | -56.7681 |
| avg_hold_time_bars | 25.4839 |
| exposure | 0.7205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
