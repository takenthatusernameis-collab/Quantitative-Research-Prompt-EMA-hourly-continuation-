# EMA Hourly Continuation — MANA/USDT P12_55

**Symbol:** MANA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 608 |
| net_profit_factor | 0.7898 |
| net_win_rate | 0.5066 |
| gross_profit_factor | 1.0421 |
| gross_win_rate | 0.5066 |
| sharpe_ratio | -1.9741 |
| sortino_ratio | -0.6989 |
| max_drawdown | 0.5824 |
| cagr | -0.2750 |
| net_avg_win | 67.5914 |
| net_avg_loss | -87.8636 |
| avg_hold_time_bars | 12.7056 |
| exposure | 0.3511 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
