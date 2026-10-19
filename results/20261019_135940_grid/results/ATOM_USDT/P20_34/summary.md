# EMA Hourly Continuation — ATOM/USDT P20_34

**Symbol:** ATOM/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1088 |
| net_profit_factor | 0.2576 |
| net_win_rate | 0.3934 |
| gross_profit_factor | 0.6770 |
| gross_win_rate | 0.4338 |
| sharpe_ratio | -11.4851 |
| sortino_ratio | -5.4436 |
| max_drawdown | 0.9991 |
| cagr | -0.9374 |
| net_avg_win | 8.0997 |
| net_avg_loss | -20.3897 |
| avg_hold_time_bars | 2.6360 |
| exposure | 0.1304 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
