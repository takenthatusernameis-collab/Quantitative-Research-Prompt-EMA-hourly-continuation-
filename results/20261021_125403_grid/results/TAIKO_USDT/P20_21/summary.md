# EMA Hourly Continuation — TAIKO/USDT P20_21

**Symbol:** TAIKO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 156 |
| net_profit_factor | 0.7719 |
| net_win_rate | 0.5385 |
| gross_profit_factor | 1.1733 |
| gross_win_rate | 0.5385 |
| sharpe_ratio | -1.0772 |
| sortino_ratio | -0.1995 |
| max_drawdown | 0.2841 |
| cagr | -0.0882 |
| net_avg_win | 79.3265 |
| net_avg_loss | -119.9025 |
| avg_hold_time_bars | 6.1410 |
| exposure | 0.0460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
