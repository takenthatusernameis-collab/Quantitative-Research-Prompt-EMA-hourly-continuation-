# EMA Hourly Continuation — UNI/USDT P100_144

**Symbol:** UNI/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.5159 |
| net_win_rate | 0.4725 |
| gross_profit_factor | 0.9307 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -4.8094 |
| sortino_ratio | -1.5018 |
| max_drawdown | 0.8515 |
| cagr | -0.5248 |
| net_avg_win | 38.8510 |
| net_avg_loss | -67.4522 |
| avg_hold_time_bars | 4.2200 |
| exposure | 0.0942 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
