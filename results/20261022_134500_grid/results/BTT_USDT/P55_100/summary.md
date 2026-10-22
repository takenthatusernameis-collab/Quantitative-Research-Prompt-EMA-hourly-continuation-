# EMA Hourly Continuation — BTT/USDT P55_100

**Symbol:** BTT/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 651 |
| net_profit_factor | 0.2863 |
| net_win_rate | 0.3349 |
| gross_profit_factor | 0.7570 |
| gross_win_rate | 0.4025 |
| sharpe_ratio | -11.3873 |
| sortino_ratio | -4.3052 |
| max_drawdown | 0.9970 |
| cagr | -0.9015 |
| net_avg_win | 18.3472 |
| net_avg_loss | -32.2633 |
| avg_hold_time_bars | 5.9386 |
| exposure | 0.1757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
