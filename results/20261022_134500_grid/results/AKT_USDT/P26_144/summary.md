# EMA Hourly Continuation — AKT/USDT P26_144

**Symbol:** AKT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 536 |
| net_profit_factor | 0.7062 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 1.0180 |
| gross_win_rate | 0.5075 |
| sharpe_ratio | -2.5450 |
| sortino_ratio | -0.8247 |
| max_drawdown | 0.6557 |
| cagr | -0.3292 |
| net_avg_win | 56.9935 |
| net_avg_loss | -80.1062 |
| avg_hold_time_bars | 17.7052 |
| exposure | 0.4314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
