# EMA Hourly Continuation — CHR/USDT P50_100

**Symbol:** CHR/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.6700 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.8625 |
| gross_win_rate | 0.4674 |
| sharpe_ratio | -2.6000 |
| sortino_ratio | -0.7929 |
| max_drawdown | 0.6437 |
| cagr | -0.3051 |
| net_avg_win | 56.7348 |
| net_avg_loss | -74.3064 |
| avg_hold_time_bars | 7.9130 |
| exposure | 0.1647 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
