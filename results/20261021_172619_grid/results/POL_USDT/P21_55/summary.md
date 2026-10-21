# EMA Hourly Continuation — POL/USDT P21_55

**Symbol:** POL/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.6612 |
| net_win_rate | 0.4852 |
| gross_profit_factor | 0.9048 |
| gross_win_rate | 0.4852 |
| sharpe_ratio | -2.5448 |
| sortino_ratio | -0.7929 |
| max_drawdown | 0.6154 |
| cagr | -0.3051 |
| net_avg_win | 50.8395 |
| net_avg_loss | -72.4736 |
| avg_hold_time_bars | 10.4262 |
| exposure | 0.2246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
