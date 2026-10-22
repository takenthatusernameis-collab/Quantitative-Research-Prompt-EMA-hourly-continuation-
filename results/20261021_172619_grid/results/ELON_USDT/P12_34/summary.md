# EMA Hourly Continuation — ELON/USDT P12_34

**Symbol:** ELON/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.6578 |
| net_win_rate | 0.4707 |
| gross_profit_factor | 0.8925 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -3.1642 |
| sortino_ratio | -1.0399 |
| max_drawdown | 0.7019 |
| cagr | -0.3784 |
| net_avg_win | 53.8044 |
| net_avg_loss | -72.7415 |
| avg_hold_time_bars | 8.1474 |
| exposure | 0.1959 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
