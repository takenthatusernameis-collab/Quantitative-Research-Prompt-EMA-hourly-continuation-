# EMA Hourly Continuation — CHZ/USDT P26_55

**Symbol:** CHZ/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 892 |
| net_profit_factor | 0.4734 |
| net_win_rate | 0.4529 |
| gross_profit_factor | 0.8750 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -7.2198 |
| sortino_ratio | -3.0390 |
| max_drawdown | 0.9772 |
| cagr | -0.7775 |
| net_avg_win | 21.7439 |
| net_avg_loss | -38.0223 |
| avg_hold_time_bars | 4.5908 |
| exposure | 0.1861 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
