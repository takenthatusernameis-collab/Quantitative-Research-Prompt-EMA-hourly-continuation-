# EMA Hourly Continuation — OP/USDT P20_200

**Symbol:** OP/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.8019 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9411 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -1.1242 |
| sortino_ratio | -0.2605 |
| max_drawdown | 0.3064 |
| cagr | -0.1141 |
| net_avg_win | 82.3320 |
| net_avg_loss | -97.3821 |
| avg_hold_time_bars | 53.7434 |
| exposure | 0.6474 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
