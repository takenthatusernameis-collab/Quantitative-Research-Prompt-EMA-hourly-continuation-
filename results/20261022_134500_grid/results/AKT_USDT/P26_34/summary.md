# EMA Hourly Continuation — AKT/USDT P26_34

**Symbol:** AKT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1012 |
| net_profit_factor | 0.3463 |
| net_win_rate | 0.3982 |
| gross_profit_factor | 0.8451 |
| gross_win_rate | 0.4298 |
| sharpe_ratio | -11.1754 |
| sortino_ratio | -5.0956 |
| max_drawdown | 0.9987 |
| cagr | -0.9287 |
| net_avg_win | 13.1291 |
| net_avg_loss | -25.0868 |
| avg_hold_time_bars | 2.1996 |
| exposure | 0.1012 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
