# EMA Hourly Continuation — NEO/USDT P26_100

**Symbol:** NEO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.6680 |
| net_win_rate | 0.4773 |
| gross_profit_factor | 0.8956 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -2.5421 |
| sortino_ratio | -0.7612 |
| max_drawdown | 0.6050 |
| cagr | -0.2940 |
| net_avg_win | 55.8473 |
| net_avg_loss | -76.3330 |
| avg_hold_time_bars | 18.7864 |
| exposure | 0.3757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
