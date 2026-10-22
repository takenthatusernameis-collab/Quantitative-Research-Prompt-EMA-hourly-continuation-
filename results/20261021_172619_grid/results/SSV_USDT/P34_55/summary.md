# EMA Hourly Continuation — SSV/USDT P34_55

**Symbol:** SSV/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.6775 |
| net_win_rate | 0.4757 |
| gross_profit_factor | 0.9242 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -2.5453 |
| sortino_ratio | -0.7178 |
| max_drawdown | 0.5717 |
| cagr | -0.2804 |
| net_avg_win | 63.6936 |
| net_avg_loss | -85.2993 |
| avg_hold_time_bars | 6.1023 |
| exposure | 0.1080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
