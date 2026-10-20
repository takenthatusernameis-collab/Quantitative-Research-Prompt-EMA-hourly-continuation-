# EMA Hourly Continuation — KAVA/USDT P20_89

**Symbol:** KAVA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 723 |
| net_profit_factor | 0.5267 |
| net_win_rate | 0.4412 |
| gross_profit_factor | 0.9237 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -6.2584 |
| sortino_ratio | -2.3578 |
| max_drawdown | 0.9511 |
| cagr | -0.6906 |
| net_avg_win | 33.0484 |
| net_avg_loss | -49.5474 |
| avg_hold_time_bars | 13.3389 |
| exposure | 0.4384 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
