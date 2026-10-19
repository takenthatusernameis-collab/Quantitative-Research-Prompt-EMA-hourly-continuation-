# EMA Hourly Continuation — CAKE/USDT P34_89

**Symbol:** CAKE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.5096 |
| net_win_rate | 0.4864 |
| gross_profit_factor | 0.9513 |
| gross_win_rate | 0.5085 |
| sharpe_ratio | -4.6092 |
| sortino_ratio | -1.5702 |
| max_drawdown | 0.8733 |
| cagr | -0.5409 |
| net_avg_win | 31.0778 |
| net_avg_loss | -57.7685 |
| avg_hold_time_bars | 10.0136 |
| exposure | 0.2685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
