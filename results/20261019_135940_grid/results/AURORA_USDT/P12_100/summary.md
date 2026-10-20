# EMA Hourly Continuation — AURORA/USDT P12_100

**Symbol:** AURORA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 573 |
| net_profit_factor | 0.6303 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9520 |
| gross_win_rate | 0.4834 |
| sharpe_ratio | -3.6660 |
| sortino_ratio | -1.2211 |
| max_drawdown | 0.7812 |
| cagr | -0.4499 |
| net_avg_win | 48.1683 |
| net_avg_loss | -70.5267 |
| avg_hold_time_bars | 21.0419 |
| exposure | 0.5480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
