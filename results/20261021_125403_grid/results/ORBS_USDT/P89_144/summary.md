# EMA Hourly Continuation — ORBS/USDT P89_144

**Symbol:** ORBS/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.6251 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.9347 |
| gross_win_rate | 0.4759 |
| sharpe_ratio | -2.7671 |
| sortino_ratio | -0.6996 |
| max_drawdown | 0.5573 |
| cagr | -0.2748 |
| net_avg_win | 62.7976 |
| net_avg_loss | -90.0515 |
| avg_hold_time_bars | 8.7492 |
| exposure | 0.1237 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
