# EMA Hourly Continuation — AKT/USDT P21_144

**Symbol:** AKT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.7247 |
| net_win_rate | 0.5038 |
| gross_profit_factor | 1.0428 |
| gross_win_rate | 0.5096 |
| sharpe_ratio | -2.4006 |
| sortino_ratio | -0.7674 |
| max_drawdown | 0.6358 |
| cagr | -0.3102 |
| net_avg_win | 60.9156 |
| net_avg_loss | -85.3649 |
| avg_hold_time_bars | 21.3731 |
| exposure | 0.5052 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
