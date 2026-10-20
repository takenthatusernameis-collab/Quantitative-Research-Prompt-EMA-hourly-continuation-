# EMA Hourly Continuation — ROSE/USDT P12_34

**Symbol:** ROSE/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1364 |
| net_profit_factor | 0.4427 |
| net_win_rate | 0.4406 |
| gross_profit_factor | 0.7999 |
| gross_win_rate | 0.4501 |
| sharpe_ratio | -9.0716 |
| sortino_ratio | -4.7045 |
| max_drawdown | 0.9971 |
| cagr | -0.9025 |
| net_avg_win | 13.1790 |
| net_avg_loss | -23.4491 |
| avg_hold_time_bars | 3.9641 |
| exposure | 0.2458 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
