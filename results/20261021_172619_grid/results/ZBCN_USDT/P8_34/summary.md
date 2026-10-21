# EMA Hourly Continuation — ZBCN/USDT P8_34

**Symbol:** ZBCN/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.9719 |
| net_win_rate | 0.5433 |
| gross_profit_factor | 1.1804 |
| gross_win_rate | 0.5433 |
| sharpe_ratio | -0.1501 |
| sortino_ratio | -0.0568 |
| max_drawdown | 0.3064 |
| cagr | -0.0376 |
| net_avg_win | 85.7439 |
| net_avg_loss | -104.9427 |
| avg_hold_time_bars | 8.1522 |
| exposure | 0.2527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
