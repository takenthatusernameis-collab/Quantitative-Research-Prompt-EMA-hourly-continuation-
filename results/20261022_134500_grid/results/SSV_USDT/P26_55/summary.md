# EMA Hourly Continuation — SSV/USDT P26_55

**Symbol:** SSV/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 996 |
| net_profit_factor | 0.5346 |
| net_win_rate | 0.4398 |
| gross_profit_factor | 0.8861 |
| gross_win_rate | 0.4588 |
| sharpe_ratio | -7.3846 |
| sortino_ratio | -3.2751 |
| max_drawdown | 0.9835 |
| cagr | -0.7990 |
| net_avg_win | 25.7644 |
| net_avg_loss | -37.8318 |
| avg_hold_time_bars | 4.4588 |
| exposure | 0.2010 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
