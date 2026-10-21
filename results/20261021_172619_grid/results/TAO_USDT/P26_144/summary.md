# EMA Hourly Continuation — TAO/USDT P26_144

**Symbol:** TAO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.9281 |
| net_win_rate | 0.5201 |
| gross_profit_factor | 1.0823 |
| gross_win_rate | 0.5201 |
| sharpe_ratio | -0.4111 |
| sortino_ratio | -0.1103 |
| max_drawdown | 0.2418 |
| cagr | -0.0540 |
| net_avg_win | 92.7354 |
| net_avg_loss | -108.2957 |
| avg_hold_time_bars | 28.3937 |
| exposure | 0.4491 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
