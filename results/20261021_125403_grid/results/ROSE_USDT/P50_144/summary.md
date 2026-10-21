# EMA Hourly Continuation — ROSE/USDT P50_144

**Symbol:** ROSE/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.8649 |
| net_win_rate | 0.5165 |
| gross_profit_factor | 1.0572 |
| gross_win_rate | 0.5165 |
| sharpe_ratio | -0.8205 |
| sortino_ratio | -0.2251 |
| max_drawdown | 0.2678 |
| cagr | -0.1007 |
| net_avg_win | 79.6858 |
| net_avg_loss | -98.4188 |
| avg_hold_time_bars | 17.2115 |
| exposure | 0.2848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
