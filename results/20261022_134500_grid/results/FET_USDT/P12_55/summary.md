# EMA Hourly Continuation — FET/USDT P12_55

**Symbol:** FET/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1014 |
| net_profit_factor | 0.6044 |
| net_win_rate | 0.4813 |
| gross_profit_factor | 0.9194 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -5.0126 |
| sortino_ratio | -2.2448 |
| max_drawdown | 0.9353 |
| cagr | -0.6595 |
| net_avg_win | 29.2136 |
| net_avg_loss | -44.8435 |
| avg_hold_time_bars | 8.2623 |
| exposure | 0.3808 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
