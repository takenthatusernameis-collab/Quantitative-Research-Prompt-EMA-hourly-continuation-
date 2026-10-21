# EMA Hourly Continuation — NEAR/USDT P20_100

**Symbol:** NEAR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.7678 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 0.9212 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -1.7028 |
| sortino_ratio | -0.5033 |
| max_drawdown | 0.4915 |
| cagr | -0.2079 |
| net_avg_win | 70.8011 |
| net_avg_loss | -85.5924 |
| avg_hold_time_bars | 20.0116 |
| exposure | 0.3911 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
