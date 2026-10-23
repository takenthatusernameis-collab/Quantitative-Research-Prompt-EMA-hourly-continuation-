# EMA Hourly Continuation — QI/USDT P8_34

**Symbol:** QI/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1219 |
| net_profit_factor | 0.5080 |
| net_win_rate | 0.4520 |
| gross_profit_factor | 0.8978 |
| gross_win_rate | 0.4709 |
| sharpe_ratio | -7.4062 |
| sortino_ratio | -3.6346 |
| max_drawdown | 0.9882 |
| cagr | -0.8280 |
| net_avg_win | 18.5181 |
| net_avg_loss | -30.0681 |
| avg_hold_time_bars | 6.3929 |
| exposure | 0.3526 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
