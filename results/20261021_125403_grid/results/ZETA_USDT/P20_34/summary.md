# EMA Hourly Continuation — ZETA/USDT P20_34

**Symbol:** ZETA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.6126 |
| net_win_rate | 0.4736 |
| gross_profit_factor | 0.8720 |
| gross_win_rate | 0.4736 |
| sharpe_ratio | -3.0222 |
| sortino_ratio | -0.8807 |
| max_drawdown | 0.6572 |
| cagr | -0.3304 |
| net_avg_win | 51.0802 |
| net_avg_loss | -75.0060 |
| avg_hold_time_bars | 5.1106 |
| exposure | 0.0962 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
