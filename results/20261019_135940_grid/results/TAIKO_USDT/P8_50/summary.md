# EMA Hourly Continuation — TAIKO/USDT P8_50

**Symbol:** TAIKO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1022 |
| net_profit_factor | 0.6536 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 1.0160 |
| gross_win_rate | 0.4941 |
| sharpe_ratio | -5.5125 |
| sortino_ratio | -2.5520 |
| max_drawdown | 0.9531 |
| cagr | -0.7070 |
| net_avg_win | 36.2755 |
| net_avg_loss | -51.5220 |
| avg_hold_time_bars | 9.5930 |
| exposure | 0.4709 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
