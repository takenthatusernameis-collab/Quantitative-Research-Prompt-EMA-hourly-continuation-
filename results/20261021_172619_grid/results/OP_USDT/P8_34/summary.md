# EMA Hourly Continuation — OP/USDT P8_34

**Symbol:** OP/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.7668 |
| net_win_rate | 0.5028 |
| gross_profit_factor | 0.9891 |
| gross_win_rate | 0.5028 |
| sharpe_ratio | -2.0552 |
| sortino_ratio | -0.7823 |
| max_drawdown | 0.6306 |
| cagr | -0.3027 |
| net_avg_win | 55.3294 |
| net_avg_loss | -72.9782 |
| avg_hold_time_bars | 9.3636 |
| exposure | 0.2996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
