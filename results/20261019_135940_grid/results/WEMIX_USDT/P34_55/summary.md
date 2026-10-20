# EMA Hourly Continuation — WEMIX/USDT P34_55

**Symbol:** WEMIX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1378 |
| net_profit_factor | 0.0860 |
| net_win_rate | 0.2453 |
| gross_profit_factor | 0.2248 |
| gross_win_rate | 0.2779 |
| sharpe_ratio | -19.0888 |
| sortino_ratio | -10.4895 |
| max_drawdown | 1.0000 |
| cagr | -0.9960 |
| net_avg_win | 2.7851 |
| net_avg_loss | -10.5205 |
| avg_hold_time_bars | 2.8454 |
| exposure | 0.1782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
