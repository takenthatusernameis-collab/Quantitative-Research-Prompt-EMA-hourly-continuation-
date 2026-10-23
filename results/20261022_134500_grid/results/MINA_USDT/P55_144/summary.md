# EMA Hourly Continuation — MINA/USDT P55_144

**Symbol:** MINA/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.5806 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.8880 |
| gross_win_rate | 0.4733 |
| sharpe_ratio | -3.6899 |
| sortino_ratio | -1.1498 |
| max_drawdown | 0.7564 |
| cagr | -0.4215 |
| net_avg_win | 45.3628 |
| net_avg_loss | -69.0438 |
| avg_hold_time_bars | 12.1420 |
| exposure | 0.2682 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
