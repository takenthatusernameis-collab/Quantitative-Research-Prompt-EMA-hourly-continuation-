# EMA Hourly Continuation — WLD/USDT P100_144

**Symbol:** WLD/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 190 |
| net_profit_factor | 0.9777 |
| net_win_rate | 0.5526 |
| gross_profit_factor | 1.2228 |
| gross_win_rate | 0.5526 |
| sharpe_ratio | -0.0544 |
| sortino_ratio | -0.0109 |
| max_drawdown | 0.1048 |
| cagr | -0.0085 |
| net_avg_win | 88.4718 |
| net_avg_loss | -111.7785 |
| avg_hold_time_bars | 8.2526 |
| exposure | 0.0713 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
