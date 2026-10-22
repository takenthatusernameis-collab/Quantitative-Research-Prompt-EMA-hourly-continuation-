# EMA Hourly Continuation — QNT/USDT P8_34

**Symbol:** QNT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1540 |
| net_profit_factor | 0.3770 |
| net_win_rate | 0.4357 |
| gross_profit_factor | 0.7986 |
| gross_win_rate | 0.4578 |
| sharpe_ratio | -10.5427 |
| sortino_ratio | -5.8466 |
| max_drawdown | 0.9993 |
| cagr | -0.9450 |
| net_avg_win | 9.0109 |
| net_avg_loss | -18.4573 |
| avg_hold_time_bars | 4.6058 |
| exposure | 0.3224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
