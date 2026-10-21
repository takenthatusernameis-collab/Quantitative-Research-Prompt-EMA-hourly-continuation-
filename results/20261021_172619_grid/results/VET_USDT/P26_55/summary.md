# EMA Hourly Continuation — VET/USDT P26_55

**Symbol:** VET/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.7190 |
| net_win_rate | 0.4977 |
| gross_profit_factor | 1.0144 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.3614 |
| sortino_ratio | -0.7123 |
| max_drawdown | 0.5754 |
| cagr | -0.2777 |
| net_avg_win | 64.9311 |
| net_avg_loss | -89.4929 |
| avg_hold_time_bars | 6.4977 |
| exposure | 0.1305 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
