# EMA Hourly Continuation — NEAR/USDT P20_144

**Symbol:** NEAR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.6943 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 0.9587 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -2.7036 |
| sortino_ratio | -0.8405 |
| max_drawdown | 0.6488 |
| cagr | -0.3284 |
| net_avg_win | 61.6007 |
| net_avg_loss | -81.7096 |
| avg_hold_time_bars | 23.7942 |
| exposure | 0.5256 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
