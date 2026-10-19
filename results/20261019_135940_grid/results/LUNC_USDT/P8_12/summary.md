# EMA Hourly Continuation — LUNC/USDT P8_12

**Symbol:** LUNC/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1968 |
| net_profit_factor | 0.1446 |
| net_win_rate | 0.3354 |
| gross_profit_factor | 0.5880 |
| gross_win_rate | 0.3902 |
| sharpe_ratio | -21.0679 |
| sortino_ratio | -13.8059 |
| max_drawdown | 1.0000 |
| cagr | -0.9995 |
| net_avg_win | 2.5615 |
| net_avg_loss | -8.9378 |
| avg_hold_time_bars | 1.6560 |
| exposure | 0.1481 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
