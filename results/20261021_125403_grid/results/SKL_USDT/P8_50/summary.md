# EMA Hourly Continuation — SKL/USDT P8_50

**Symbol:** SKL/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 752 |
| net_profit_factor | 0.7862 |
| net_win_rate | 0.4854 |
| gross_profit_factor | 0.9860 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -2.5507 |
| sortino_ratio | -0.9991 |
| max_drawdown | 0.7199 |
| cagr | -0.3685 |
| net_avg_win | 68.9744 |
| net_avg_loss | -82.7465 |
| avg_hold_time_bars | 12.6410 |
| exposure | 0.4321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
