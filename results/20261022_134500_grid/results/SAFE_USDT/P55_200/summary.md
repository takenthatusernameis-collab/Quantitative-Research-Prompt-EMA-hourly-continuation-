# EMA Hourly Continuation — SAFE/USDT P55_200

**Symbol:** SAFE/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.6897 |
| net_win_rate | 0.4854 |
| gross_profit_factor | 0.9861 |
| gross_win_rate | 0.4907 |
| sharpe_ratio | -2.3501 |
| sortino_ratio | -0.6467 |
| max_drawdown | 0.5429 |
| cagr | -0.2633 |
| net_avg_win | 64.7597 |
| net_avg_loss | -88.5699 |
| avg_hold_time_bars | 22.1088 |
| exposure | 0.3817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
