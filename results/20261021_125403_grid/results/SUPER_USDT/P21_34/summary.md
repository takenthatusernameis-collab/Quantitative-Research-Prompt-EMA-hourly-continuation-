# EMA Hourly Continuation — SUPER/USDT P21_34

**Symbol:** SUPER/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.6745 |
| net_win_rate | 0.4972 |
| gross_profit_factor | 0.9835 |
| gross_win_rate | 0.5028 |
| sharpe_ratio | -2.2806 |
| sortino_ratio | -0.6179 |
| max_drawdown | 0.5258 |
| cagr | -0.2481 |
| net_avg_win | 59.5095 |
| net_avg_loss | -87.2536 |
| avg_hold_time_bars | 5.2682 |
| exposure | 0.0857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
