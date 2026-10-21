# EMA Hourly Continuation — ID/USDT P20_55

**Symbol:** ID/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 600 |
| net_profit_factor | 0.7033 |
| net_win_rate | 0.4850 |
| gross_profit_factor | 0.9606 |
| gross_win_rate | 0.4850 |
| sharpe_ratio | -2.8785 |
| sortino_ratio | -1.0051 |
| max_drawdown | 0.7024 |
| cagr | -0.3697 |
| net_avg_win | 56.0365 |
| net_avg_loss | -75.0338 |
| avg_hold_time_bars | 8.5167 |
| exposure | 0.2313 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
