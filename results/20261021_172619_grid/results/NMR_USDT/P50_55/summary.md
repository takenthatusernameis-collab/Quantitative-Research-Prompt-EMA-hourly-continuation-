# EMA Hourly Continuation — NMR/USDT P50_55

**Symbol:** NMR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 160 |
| net_profit_factor | 0.5920 |
| net_win_rate | 0.4688 |
| gross_profit_factor | 0.9400 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -2.1182 |
| sortino_ratio | -0.3852 |
| max_drawdown | 0.3821 |
| cagr | -0.1597 |
| net_avg_win | 68.4969 |
| net_avg_loss | -102.0947 |
| avg_hold_time_bars | 5.0875 |
| exposure | 0.0370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
