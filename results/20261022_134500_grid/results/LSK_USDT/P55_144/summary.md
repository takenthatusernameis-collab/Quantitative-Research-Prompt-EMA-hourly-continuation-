# EMA Hourly Continuation — LSK/USDT P55_144

**Symbol:** LSK/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.6297 |
| net_win_rate | 0.4978 |
| gross_profit_factor | 0.9517 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.6686 |
| sortino_ratio | -0.8075 |
| max_drawdown | 0.6582 |
| cagr | -0.3140 |
| net_avg_win | 46.2433 |
| net_avg_loss | -72.7938 |
| avg_hold_time_bars | 13.2566 |
| exposure | 0.2724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
