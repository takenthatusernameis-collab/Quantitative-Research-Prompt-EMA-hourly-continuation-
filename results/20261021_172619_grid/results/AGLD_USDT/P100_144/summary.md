# EMA Hourly Continuation — AGLD/USDT P100_144

**Symbol:** AGLD/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.6054 |
| net_win_rate | 0.4427 |
| gross_profit_factor | 0.8355 |
| gross_win_rate | 0.4427 |
| sharpe_ratio | -3.0328 |
| sortino_ratio | -0.7635 |
| max_drawdown | 0.5906 |
| cagr | -0.2960 |
| net_avg_win | 64.8467 |
| net_avg_loss | -85.0734 |
| avg_hold_time_bars | 7.4172 |
| exposure | 0.1054 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
