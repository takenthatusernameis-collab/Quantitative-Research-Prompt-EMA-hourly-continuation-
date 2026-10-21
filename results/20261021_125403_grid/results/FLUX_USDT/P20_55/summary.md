# EMA Hourly Continuation — FLUX/USDT P20_55

**Symbol:** FLUX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 538 |
| net_profit_factor | 0.7223 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.9453 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -2.5854 |
| sortino_ratio | -0.8573 |
| max_drawdown | 0.6577 |
| cagr | -0.3245 |
| net_avg_win | 63.1734 |
| net_avg_loss | -80.5876 |
| avg_hold_time_bars | 7.3030 |
| exposure | 0.1786 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
