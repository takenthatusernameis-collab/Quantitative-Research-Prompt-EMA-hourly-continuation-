# EMA Hourly Continuation — XLM/USDT P26_55

**Symbol:** XLM/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.6256 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 0.9455 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -2.5981 |
| sortino_ratio | -0.7492 |
| max_drawdown | 0.5859 |
| cagr | -0.2899 |
| net_avg_win | 48.4348 |
| net_avg_loss | -75.5209 |
| avg_hold_time_bars | 7.6898 |
| exposure | 0.1409 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
