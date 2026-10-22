# EMA Hourly Continuation — GRAM/USDT P55_144

**Symbol:** GRAM/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.3814 |
| net_win_rate | 0.4327 |
| gross_profit_factor | 0.7415 |
| gross_win_rate | 0.4442 |
| sharpe_ratio | -5.8907 |
| sortino_ratio | -1.8753 |
| max_drawdown | 0.9136 |
| cagr | -0.6163 |
| net_avg_win | 24.9260 |
| net_avg_loss | -49.8524 |
| avg_hold_time_bars | 9.9750 |
| exposure | 0.2358 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
