# EMA Hourly Continuation — LUNC/USDT P8_20

**Symbol:** LUNC/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1848 |
| net_profit_factor | 0.3247 |
| net_win_rate | 0.4048 |
| gross_profit_factor | 0.8430 |
| gross_win_rate | 0.4313 |
| sharpe_ratio | -14.8810 |
| sortino_ratio | -9.1025 |
| max_drawdown | 1.0000 |
| cagr | -0.9909 |
| net_avg_win | 6.4279 |
| net_avg_loss | -13.4618 |
| avg_hold_time_bars | 2.4940 |
| exposure | 0.2095 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
