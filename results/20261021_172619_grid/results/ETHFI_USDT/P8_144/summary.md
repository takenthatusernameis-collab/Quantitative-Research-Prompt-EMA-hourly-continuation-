# EMA Hourly Continuation — ETHFI/USDT P8_144

**Symbol:** ETHFI/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.8107 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.9256 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -1.3380 |
| sortino_ratio | -0.3561 |
| max_drawdown | 0.4033 |
| cagr | -0.1525 |
| net_avg_win | 87.1985 |
| net_avg_loss | -98.1522 |
| avg_hold_time_bars | 47.2686 |
| exposure | 0.7520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
