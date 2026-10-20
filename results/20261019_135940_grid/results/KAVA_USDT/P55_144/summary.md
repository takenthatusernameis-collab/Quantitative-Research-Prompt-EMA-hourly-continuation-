# EMA Hourly Continuation — KAVA/USDT P55_144

**Symbol:** KAVA/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.4540 |
| net_win_rate | 0.4145 |
| gross_profit_factor | 0.8063 |
| gross_win_rate | 0.4487 |
| sharpe_ratio | -5.8671 |
| sortino_ratio | -1.8341 |
| max_drawdown | 0.9037 |
| cagr | -0.6035 |
| net_avg_win | 36.4160 |
| net_avg_loss | -56.7762 |
| avg_hold_time_bars | 12.5111 |
| exposure | 0.2826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
