# EMA Hourly Continuation — AMP/USDT P89_144

**Symbol:** AMP/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.4607 |
| net_win_rate | 0.4106 |
| gross_profit_factor | 0.6446 |
| gross_win_rate | 0.4106 |
| sharpe_ratio | -3.7348 |
| sortino_ratio | -0.9233 |
| max_drawdown | 0.6783 |
| cagr | -0.3482 |
| net_avg_win | 45.3837 |
| net_avg_loss | -68.6213 |
| avg_hold_time_bars | 8.2086 |
| exposure | 0.1127 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
