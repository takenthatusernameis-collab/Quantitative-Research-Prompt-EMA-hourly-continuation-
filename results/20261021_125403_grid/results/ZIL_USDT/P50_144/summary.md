# EMA Hourly Continuation — ZIL/USDT P50_144

**Symbol:** ZIL/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.7719 |
| net_win_rate | 0.5014 |
| gross_profit_factor | 1.0126 |
| gross_win_rate | 0.5014 |
| sharpe_ratio | -1.6265 |
| sortino_ratio | -0.4477 |
| max_drawdown | 0.4351 |
| cagr | -0.1862 |
| net_avg_win | 73.8696 |
| net_avg_loss | -96.2246 |
| avg_hold_time_bars | 18.2683 |
| exposure | 0.3064 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
