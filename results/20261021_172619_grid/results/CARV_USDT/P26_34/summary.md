# EMA Hourly Continuation — CARV/USDT P26_34

**Symbol:** CARV/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 246 |
| net_profit_factor | 0.6035 |
| net_win_rate | 0.4878 |
| gross_profit_factor | 0.9198 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -2.5511 |
| sortino_ratio | -0.6399 |
| max_drawdown | 0.4714 |
| cagr | -0.2528 |
| net_avg_win | 56.6159 |
| net_avg_loss | -89.3406 |
| avg_hold_time_bars | 6.4715 |
| exposure | 0.0896 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
