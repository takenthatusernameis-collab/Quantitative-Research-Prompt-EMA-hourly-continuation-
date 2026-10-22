# EMA Hourly Continuation — EGLD/USDT P8_26

**Symbol:** EGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1530 |
| net_profit_factor | 0.3833 |
| net_win_rate | 0.4314 |
| gross_profit_factor | 0.8418 |
| gross_win_rate | 0.4542 |
| sharpe_ratio | -10.8266 |
| sortino_ratio | -5.9669 |
| max_drawdown | 0.9994 |
| cagr | -0.9495 |
| net_avg_win | 9.4112 |
| net_avg_loss | -18.6274 |
| avg_hold_time_bars | 3.7922 |
| exposure | 0.2637 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
