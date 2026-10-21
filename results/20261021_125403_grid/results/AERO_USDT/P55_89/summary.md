# EMA Hourly Continuation — AERO/USDT P55_89

**Symbol:** AERO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.7329 |
| net_win_rate | 0.4834 |
| gross_profit_factor | 0.9374 |
| gross_win_rate | 0.4834 |
| sharpe_ratio | -1.6270 |
| sortino_ratio | -0.3828 |
| max_drawdown | 0.3790 |
| cagr | -0.1614 |
| net_avg_win | 74.8057 |
| net_avg_loss | -95.5128 |
| avg_hold_time_bars | 7.3653 |
| exposure | 0.0907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
