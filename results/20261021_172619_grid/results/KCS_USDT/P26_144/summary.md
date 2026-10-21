# EMA Hourly Continuation — KCS/USDT P26_144

**Symbol:** KCS/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.5347 |
| net_win_rate | 0.4522 |
| gross_profit_factor | 0.8504 |
| gross_win_rate | 0.4522 |
| sharpe_ratio | -3.6859 |
| sortino_ratio | -0.9947 |
| max_drawdown | 0.6875 |
| cagr | -0.3662 |
| net_avg_win | 48.6693 |
| net_avg_loss | -75.1513 |
| avg_hold_time_bars | 28.4860 |
| exposure | 0.4610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
