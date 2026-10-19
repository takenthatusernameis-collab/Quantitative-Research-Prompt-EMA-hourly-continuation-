# EMA Hourly Continuation — HBAR/USDT P34_144

**Symbol:** HBAR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.6751 |
| net_win_rate | 0.4913 |
| gross_profit_factor | 1.0398 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -3.0516 |
| sortino_ratio | -0.9829 |
| max_drawdown | 0.7006 |
| cagr | -0.3742 |
| net_avg_win | 56.3674 |
| net_avg_loss | -80.6519 |
| avg_hold_time_bars | 15.0674 |
| exposure | 0.3555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
