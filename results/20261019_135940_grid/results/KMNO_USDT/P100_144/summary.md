# EMA Hourly Continuation — KMNO/USDT P100_144

**Symbol:** KMNO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.5324 |
| net_win_rate | 0.4758 |
| gross_profit_factor | 0.9161 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -4.0211 |
| sortino_ratio | -1.1965 |
| max_drawdown | 0.7716 |
| cagr | -0.4373 |
| net_avg_win | 41.9367 |
| net_avg_loss | -71.4807 |
| avg_hold_time_bars | 5.5797 |
| exposure | 0.1115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
