# EMA Hourly Continuation — CVX/USDT P8_26

**Symbol:** CVX/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1531 |
| net_profit_factor | 0.4460 |
| net_win_rate | 0.4396 |
| gross_profit_factor | 0.8131 |
| gross_win_rate | 0.4579 |
| sharpe_ratio | -9.2093 |
| sortino_ratio | -5.0783 |
| max_drawdown | 0.9980 |
| cagr | -0.9153 |
| net_avg_win | 11.9398 |
| net_avg_loss | -20.9967 |
| avg_hold_time_bars | 4.2306 |
| exposure | 0.2944 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
