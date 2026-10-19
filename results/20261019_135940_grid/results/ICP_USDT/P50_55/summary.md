# EMA Hourly Continuation — ICP/USDT P50_55

**Symbol:** ICP/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 859 |
| net_profit_factor | 0.1692 |
| net_win_rate | 0.3434 |
| gross_profit_factor | 0.5753 |
| gross_win_rate | 0.3958 |
| sharpe_ratio | -13.5357 |
| sortino_ratio | -5.8893 |
| max_drawdown | 0.9998 |
| cagr | -0.9630 |
| net_avg_win | 6.9016 |
| net_avg_loss | -21.3359 |
| avg_hold_time_bars | 1.7579 |
| exposure | 0.0686 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
