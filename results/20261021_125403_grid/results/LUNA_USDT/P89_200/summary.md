# EMA Hourly Continuation — LUNA/USDT P89_200

**Symbol:** LUNA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.6406 |
| net_win_rate | 0.4585 |
| gross_profit_factor | 0.8291 |
| gross_win_rate | 0.4585 |
| sharpe_ratio | -2.2177 |
| sortino_ratio | -0.5253 |
| max_drawdown | 0.4594 |
| cagr | -0.2147 |
| net_avg_win | 63.8319 |
| net_avg_loss | -84.3716 |
| avg_hold_time_bars | 16.4874 |
| exposure | 0.2076 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
