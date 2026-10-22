# EMA Hourly Continuation — MEW/USDT P12_50

**Symbol:** MEW/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.7613 |
| net_win_rate | 0.4872 |
| gross_profit_factor | 0.9446 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -2.2545 |
| sortino_ratio | -0.8055 |
| max_drawdown | 0.6167 |
| cagr | -0.3098 |
| net_avg_win | 63.3383 |
| net_avg_loss | -79.0545 |
| avg_hold_time_bars | 11.9345 |
| exposure | 0.3396 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
