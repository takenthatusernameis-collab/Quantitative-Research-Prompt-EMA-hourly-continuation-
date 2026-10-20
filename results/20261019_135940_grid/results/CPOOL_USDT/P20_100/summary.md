# EMA Hourly Continuation — CPOOL/USDT P20_100

**Symbol:** CPOOL/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 736 |
| net_profit_factor | 0.6495 |
| net_win_rate | 0.4647 |
| gross_profit_factor | 0.8761 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -4.0055 |
| sortino_ratio | -1.5283 |
| max_drawdown | 0.8506 |
| cagr | -0.5181 |
| net_avg_win | 45.5279 |
| net_avg_loss | -60.8409 |
| avg_hold_time_bars | 11.3247 |
| exposure | 0.3789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
