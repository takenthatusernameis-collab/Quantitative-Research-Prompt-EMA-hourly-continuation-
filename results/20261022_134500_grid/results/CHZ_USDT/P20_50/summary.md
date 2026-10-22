# EMA Hourly Continuation — CHZ/USDT P20_50

**Symbol:** CHZ/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 991 |
| net_profit_factor | 0.4904 |
| net_win_rate | 0.4369 |
| gross_profit_factor | 0.9077 |
| gross_win_rate | 0.4480 |
| sharpe_ratio | -8.0488 |
| sortino_ratio | -3.5651 |
| max_drawdown | 0.9882 |
| cagr | -0.8295 |
| net_avg_win | 21.9612 |
| net_avg_loss | -34.7518 |
| avg_hold_time_bars | 5.0131 |
| exposure | 0.2258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
