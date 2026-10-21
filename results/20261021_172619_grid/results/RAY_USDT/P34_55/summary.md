# EMA Hourly Continuation — RAY/USDT P34_55

**Symbol:** RAY/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.7533 |
| net_win_rate | 0.5081 |
| gross_profit_factor | 1.0227 |
| gross_win_rate | 0.5081 |
| sharpe_ratio | -1.5603 |
| sortino_ratio | -0.3939 |
| max_drawdown | 0.4289 |
| cagr | -0.1657 |
| net_avg_win | 71.1213 |
| net_avg_loss | -97.5126 |
| avg_hold_time_bars | 5.5437 |
| exposure | 0.0779 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
