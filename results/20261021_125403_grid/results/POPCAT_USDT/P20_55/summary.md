# EMA Hourly Continuation — POPCAT/USDT P20_55

**Symbol:** POPCAT/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.7106 |
| net_win_rate | 0.4656 |
| gross_profit_factor | 0.8748 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -2.6024 |
| sortino_ratio | -0.8470 |
| max_drawdown | 0.5695 |
| cagr | -0.3230 |
| net_avg_win | 66.5747 |
| net_avg_loss | -81.6425 |
| avg_hold_time_bars | 8.8647 |
| exposure | 0.2112 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
