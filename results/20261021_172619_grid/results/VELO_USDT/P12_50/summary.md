# EMA Hourly Continuation — VELO/USDT P12_50

**Symbol:** VELO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.8315 |
| net_win_rate | 0.5103 |
| gross_profit_factor | 1.0062 |
| gross_win_rate | 0.5103 |
| sharpe_ratio | -1.2470 |
| sortino_ratio | -0.4496 |
| max_drawdown | 0.5069 |
| cagr | -0.1898 |
| net_avg_win | 62.9067 |
| net_avg_loss | -78.8409 |
| avg_hold_time_bars | 9.4945 |
| exposure | 0.2723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
