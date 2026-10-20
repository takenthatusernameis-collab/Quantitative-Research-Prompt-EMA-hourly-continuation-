# EMA Hourly Continuation — ORBS/USDT P50_144

**Symbol:** ORBS/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.5639 |
| net_win_rate | 0.4277 |
| gross_profit_factor | 0.9250 |
| gross_win_rate | 0.4335 |
| sharpe_ratio | -5.3785 |
| sortino_ratio | -1.7173 |
| max_drawdown | 0.8835 |
| cagr | -0.5708 |
| net_avg_win | 51.2766 |
| net_avg_loss | -67.9731 |
| avg_hold_time_bars | 13.6262 |
| exposure | 0.3215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
