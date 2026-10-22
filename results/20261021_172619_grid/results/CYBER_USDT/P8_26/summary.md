# EMA Hourly Continuation — CYBER/USDT P8_26

**Symbol:** CYBER/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 821 |
| net_profit_factor | 0.7238 |
| net_win_rate | 0.4994 |
| gross_profit_factor | 0.9928 |
| gross_win_rate | 0.5006 |
| sharpe_ratio | -3.0741 |
| sortino_ratio | -1.2627 |
| max_drawdown | 0.7698 |
| cagr | -0.4390 |
| net_avg_win | 48.9575 |
| net_avg_loss | -67.4707 |
| avg_hold_time_bars | 6.5505 |
| exposure | 0.2445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
