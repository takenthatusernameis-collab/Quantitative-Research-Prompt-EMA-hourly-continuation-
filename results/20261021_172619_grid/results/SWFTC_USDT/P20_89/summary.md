# EMA Hourly Continuation — SWFTC/USDT P20_89

**Symbol:** SWFTC/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.7648 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9596 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -1.7028 |
| sortino_ratio | -0.5112 |
| max_drawdown | 0.4535 |
| cagr | -0.2095 |
| net_avg_win | 66.8127 |
| net_avg_loss | -84.6330 |
| avg_hold_time_bars | 16.7234 |
| exposure | 0.3352 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
