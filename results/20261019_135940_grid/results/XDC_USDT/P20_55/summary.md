# EMA Hourly Continuation — XDC/USDT P20_55

**Symbol:** XDC/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1026 |
| net_profit_factor | 0.2250 |
| net_win_rate | 0.4045 |
| gross_profit_factor | 0.6349 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -11.0133 |
| sortino_ratio | -4.9862 |
| max_drawdown | 0.9987 |
| cagr | -0.9291 |
| net_avg_win | 6.9885 |
| net_avg_loss | -21.0921 |
| avg_hold_time_bars | 4.9639 |
| exposure | 0.2315 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
