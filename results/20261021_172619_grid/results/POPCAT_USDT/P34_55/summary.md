# EMA Hourly Continuation — POPCAT/USDT P34_55

**Symbol:** POPCAT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.6439 |
| net_win_rate | 0.4537 |
| gross_profit_factor | 0.8423 |
| gross_win_rate | 0.4537 |
| sharpe_ratio | -2.8796 |
| sortino_ratio | -0.7951 |
| max_drawdown | 0.5678 |
| cagr | -0.3057 |
| net_avg_win | 67.0816 |
| net_avg_loss | -86.5263 |
| avg_hold_time_bars | 5.3704 |
| exposure | 0.0919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
