# EMA Hourly Continuation — EGLD/USDT P21_26

**Symbol:** EGLD/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 192 |
| net_profit_factor | 0.5761 |
| net_win_rate | 0.4635 |
| gross_profit_factor | 0.8630 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -2.3587 |
| sortino_ratio | -0.4681 |
| max_drawdown | 0.4527 |
| cagr | -0.1939 |
| net_avg_win | 63.8336 |
| net_avg_loss | -95.7494 |
| avg_hold_time_bars | 4.9115 |
| exposure | 0.0429 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
