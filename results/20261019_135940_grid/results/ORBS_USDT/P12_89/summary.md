# EMA Hourly Continuation — ORBS/USDT P12_89

**Symbol:** ORBS/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 812 |
| net_profit_factor | 0.5564 |
| net_win_rate | 0.4421 |
| gross_profit_factor | 0.9427 |
| gross_win_rate | 0.4594 |
| sharpe_ratio | -6.2821 |
| sortino_ratio | -2.5045 |
| max_drawdown | 0.9556 |
| cagr | -0.7083 |
| net_avg_win | 33.3514 |
| net_avg_loss | -47.5053 |
| avg_hold_time_bars | 14.7340 |
| exposure | 0.5438 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
