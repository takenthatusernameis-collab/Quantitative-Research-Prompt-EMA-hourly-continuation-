# EMA Hourly Continuation — EDU/USDT P8_21

**Symbol:** EDU/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1641 |
| net_profit_factor | 0.4262 |
| net_win_rate | 0.4296 |
| gross_profit_factor | 0.8226 |
| gross_win_rate | 0.4467 |
| sharpe_ratio | -10.2939 |
| sortino_ratio | -5.8932 |
| max_drawdown | 0.9993 |
| cagr | -0.9417 |
| net_avg_win | 10.5273 |
| net_avg_loss | -18.6047 |
| avg_hold_time_bars | 3.5801 |
| exposure | 0.2658 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
