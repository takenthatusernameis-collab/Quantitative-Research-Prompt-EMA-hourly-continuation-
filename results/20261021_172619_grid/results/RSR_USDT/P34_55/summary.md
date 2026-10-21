# EMA Hourly Continuation — RSR/USDT P34_55

**Symbol:** RSR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.8267 |
| net_win_rate | 0.5219 |
| gross_profit_factor | 1.0876 |
| gross_win_rate | 0.5219 |
| sharpe_ratio | -1.0700 |
| sortino_ratio | -0.2760 |
| max_drawdown | 0.3345 |
| cagr | -0.1196 |
| net_avg_win | 78.2055 |
| net_avg_loss | -103.2586 |
| avg_hold_time_bars | 5.8625 |
| exposure | 0.0853 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
