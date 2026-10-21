# EMA Hourly Continuation — DYDX/USDT P20_34

**Symbol:** DYDX/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.7277 |
| net_win_rate | 0.4971 |
| gross_profit_factor | 1.0074 |
| gross_win_rate | 0.4971 |
| sharpe_ratio | -1.9426 |
| sortino_ratio | -0.5188 |
| max_drawdown | 0.4571 |
| cagr | -0.2102 |
| net_avg_win | 69.4710 |
| net_avg_loss | -94.3644 |
| avg_hold_time_bars | 5.0578 |
| exposure | 0.0795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
