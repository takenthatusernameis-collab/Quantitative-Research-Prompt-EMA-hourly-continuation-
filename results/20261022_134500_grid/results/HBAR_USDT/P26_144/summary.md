# EMA Hourly Continuation — HBAR/USDT P26_144

**Symbol:** HBAR/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.6683 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 1.0343 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -3.0745 |
| sortino_ratio | -0.9726 |
| max_drawdown | 0.6968 |
| cagr | -0.3707 |
| net_avg_win | 56.3099 |
| net_avg_loss | -80.6519 |
| avg_hold_time_bars | 20.2545 |
| exposure | 0.4631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
