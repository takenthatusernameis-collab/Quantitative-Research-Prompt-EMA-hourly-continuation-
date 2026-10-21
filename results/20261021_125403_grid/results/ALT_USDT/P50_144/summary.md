# EMA Hourly Continuation — ALT/USDT P50_144

**Symbol:** ALT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.6877 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.8513 |
| gross_win_rate | 0.4674 |
| sharpe_ratio | -2.0596 |
| sortino_ratio | -0.5500 |
| max_drawdown | 0.4855 |
| cagr | -0.2239 |
| net_avg_win | 62.8597 |
| net_avg_loss | -80.2201 |
| avg_hold_time_bars | 18.5212 |
| exposure | 0.2972 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
