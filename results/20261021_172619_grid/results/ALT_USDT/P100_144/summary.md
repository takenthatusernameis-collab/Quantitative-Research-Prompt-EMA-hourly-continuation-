# EMA Hourly Continuation — ALT/USDT P100_144

**Symbol:** ALT/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.7234 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 0.9752 |
| gross_win_rate | 0.4982 |
| sharpe_ratio | -1.6063 |
| sortino_ratio | -0.3805 |
| max_drawdown | 0.3675 |
| cagr | -0.1604 |
| net_avg_win | 68.3532 |
| net_avg_loss | -93.7982 |
| avg_hold_time_bars | 8.3150 |
| exposure | 0.1032 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
