# EMA Hourly Continuation — MOODENG/USDT P20_144

**Symbol:** MOODENG/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 405 |
| net_profit_factor | 0.7520 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 0.9900 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -2.2095 |
| sortino_ratio | -0.6953 |
| max_drawdown | 0.5043 |
| cagr | -0.2776 |
| net_avg_win | 74.8557 |
| net_avg_loss | -95.2144 |
| avg_hold_time_bars | 25.2494 |
| exposure | 0.5658 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
