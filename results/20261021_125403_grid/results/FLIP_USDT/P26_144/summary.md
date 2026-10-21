# EMA Hourly Continuation — FLIP/USDT P26_144

**Symbol:** FLIP/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.6220 |
| net_win_rate | 0.4479 |
| gross_profit_factor | 0.8007 |
| gross_win_rate | 0.4479 |
| sharpe_ratio | -2.6186 |
| sortino_ratio | -0.6582 |
| max_drawdown | 0.5477 |
| cagr | -0.2632 |
| net_avg_win | 62.0686 |
| net_avg_loss | -80.9715 |
| avg_hold_time_bars | 31.8423 |
| exposure | 0.4588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
