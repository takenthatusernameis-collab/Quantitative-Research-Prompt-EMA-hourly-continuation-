# EMA Hourly Continuation — ADA/USDT P8_34

**Symbol:** ADA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 694 |
| net_profit_factor | 0.7423 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9909 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.4206 |
| sortino_ratio | -0.9148 |
| max_drawdown | 0.6892 |
| cagr | -0.3432 |
| net_avg_win | 54.1358 |
| net_avg_loss | -72.9269 |
| avg_hold_time_bars | 8.2651 |
| exposure | 0.2607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
