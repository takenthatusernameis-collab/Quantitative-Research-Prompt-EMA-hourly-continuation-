# EMA Hourly Continuation — DASH/USDT P55_200

**Symbol:** DASH/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.4184 |
| net_win_rate | 0.4231 |
| gross_profit_factor | 0.7209 |
| gross_win_rate | 0.4276 |
| sharpe_ratio | -5.0034 |
| sortino_ratio | -1.4722 |
| max_drawdown | 0.8467 |
| cagr | -0.5166 |
| net_avg_win | 32.2678 |
| net_avg_loss | -56.5604 |
| avg_hold_time_bars | 16.5452 |
| exposure | 0.3324 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
