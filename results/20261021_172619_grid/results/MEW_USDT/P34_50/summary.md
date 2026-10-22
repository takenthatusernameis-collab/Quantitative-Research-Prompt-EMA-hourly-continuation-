# EMA Hourly Continuation — MEW/USDT P34_50

**Symbol:** MEW/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.6935 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9543 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -2.0516 |
| sortino_ratio | -0.5132 |
| max_drawdown | 0.4508 |
| cagr | -0.2094 |
| net_avg_win | 67.6736 |
| net_avg_loss | -93.2036 |
| avg_hold_time_bars | 4.9377 |
| exposure | 0.0685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
