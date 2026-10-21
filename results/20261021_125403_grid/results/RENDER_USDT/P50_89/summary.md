# EMA Hourly Continuation — RENDER/USDT P50_89

**Symbol:** RENDER/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.6852 |
| net_win_rate | 0.4689 |
| gross_profit_factor | 0.8909 |
| gross_win_rate | 0.4689 |
| sharpe_ratio | -2.3063 |
| sortino_ratio | -0.6190 |
| max_drawdown | 0.4785 |
| cagr | -0.2473 |
| net_avg_win | 69.8784 |
| net_avg_loss | -90.0196 |
| avg_hold_time_bars | 7.0459 |
| exposure | 0.1134 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
