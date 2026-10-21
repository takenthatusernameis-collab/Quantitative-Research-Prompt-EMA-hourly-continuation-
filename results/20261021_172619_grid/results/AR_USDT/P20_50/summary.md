# EMA Hourly Continuation — AR/USDT P20_50

**Symbol:** AR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.7032 |
| net_win_rate | 0.4787 |
| gross_profit_factor | 0.8989 |
| gross_win_rate | 0.4787 |
| sharpe_ratio | -2.4463 |
| sortino_ratio | -0.7932 |
| max_drawdown | 0.6023 |
| cagr | -0.3047 |
| net_avg_win | 57.4139 |
| net_avg_loss | -74.9689 |
| avg_hold_time_bars | 7.5291 |
| exposure | 0.1766 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
