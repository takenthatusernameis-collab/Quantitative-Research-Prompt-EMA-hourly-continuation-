# EMA Hourly Continuation — SUPER/USDT P12_21

**Symbol:** SUPER/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1465 |
| net_profit_factor | 0.4025 |
| net_win_rate | 0.4273 |
| gross_profit_factor | 0.9069 |
| gross_win_rate | 0.4587 |
| sharpe_ratio | -11.5922 |
| sortino_ratio | -6.2652 |
| max_drawdown | 0.9997 |
| cagr | -0.9600 |
| net_avg_win | 10.7586 |
| net_avg_loss | -19.9425 |
| avg_hold_time_bars | 2.4000 |
| exposure | 0.1598 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
