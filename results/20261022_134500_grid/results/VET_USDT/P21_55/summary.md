# EMA Hourly Continuation — VET/USDT P21_55

**Symbol:** VET/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 954 |
| net_profit_factor | 0.5356 |
| net_win_rate | 0.4717 |
| gross_profit_factor | 1.0237 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -6.6439 |
| sortino_ratio | -2.8856 |
| max_drawdown | 0.9736 |
| cagr | -0.7610 |
| net_avg_win | 24.9218 |
| net_avg_loss | -41.5480 |
| avg_hold_time_bars | 4.9581 |
| exposure | 0.2150 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
