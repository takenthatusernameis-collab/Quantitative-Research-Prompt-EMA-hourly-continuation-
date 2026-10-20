# EMA Hourly Continuation — SLP/USDT P26_34

**Symbol:** SLP/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1230 |
| net_profit_factor | 0.3368 |
| net_win_rate | 0.3626 |
| gross_profit_factor | 0.8661 |
| gross_win_rate | 0.4049 |
| sharpe_ratio | -14.0597 |
| sortino_ratio | -7.1691 |
| max_drawdown | 0.9999 |
| cagr | -0.9757 |
| net_avg_win | 11.3870 |
| net_avg_loss | -19.2318 |
| avg_hold_time_bars | 2.0496 |
| exposure | 0.1146 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
