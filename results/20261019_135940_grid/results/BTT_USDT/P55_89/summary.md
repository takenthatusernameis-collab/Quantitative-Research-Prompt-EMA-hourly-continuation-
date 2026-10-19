# EMA Hourly Continuation — BTT/USDT P55_89

**Symbol:** BTT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 708 |
| net_profit_factor | 0.2239 |
| net_win_rate | 0.3051 |
| gross_profit_factor | 0.6593 |
| gross_win_rate | 0.3842 |
| sharpe_ratio | -12.8547 |
| sortino_ratio | -5.1494 |
| max_drawdown | 0.9991 |
| cagr | -0.9398 |
| net_avg_win | 13.3447 |
| net_avg_loss | -26.1664 |
| avg_hold_time_bars | 4.3319 |
| exposure | 0.1394 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
