# EMA Hourly Continuation — CGPT/USDT P89_200

**Symbol:** CGPT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.6981 |
| net_win_rate | 0.5079 |
| gross_profit_factor | 1.0817 |
| gross_win_rate | 0.5184 |
| sharpe_ratio | -2.3556 |
| sortino_ratio | -0.6460 |
| max_drawdown | 0.5611 |
| cagr | -0.2676 |
| net_avg_win | 64.9795 |
| net_avg_loss | -96.0737 |
| avg_hold_time_bars | 10.3263 |
| exposure | 0.1784 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
