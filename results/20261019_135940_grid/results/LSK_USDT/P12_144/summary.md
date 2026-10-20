# EMA Hourly Continuation — LSK/USDT P12_144

**Symbol:** LSK/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.7037 |
| net_win_rate | 0.4898 |
| gross_profit_factor | 0.9963 |
| gross_win_rate | 0.4959 |
| sharpe_ratio | -2.4669 |
| sortino_ratio | -0.7712 |
| max_drawdown | 0.6339 |
| cagr | -0.3064 |
| net_avg_win | 59.4651 |
| net_avg_loss | -81.1278 |
| avg_hold_time_bars | 29.1755 |
| exposure | 0.6498 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
