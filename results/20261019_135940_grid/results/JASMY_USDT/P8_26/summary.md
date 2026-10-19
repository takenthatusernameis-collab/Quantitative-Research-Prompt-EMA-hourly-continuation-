# EMA Hourly Continuation — JASMY/USDT P8_26

**Symbol:** JASMY/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1597 |
| net_profit_factor | 0.4736 |
| net_win_rate | 0.4490 |
| gross_profit_factor | 0.8587 |
| gross_win_rate | 0.4627 |
| sharpe_ratio | -9.9478 |
| sortino_ratio | -5.5875 |
| max_drawdown | 0.9991 |
| cagr | -0.9376 |
| net_avg_win | 12.5341 |
| net_avg_loss | -21.5654 |
| avg_hold_time_bars | 3.4546 |
| exposure | 0.2508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
