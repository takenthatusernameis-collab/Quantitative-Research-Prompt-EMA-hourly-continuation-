# EMA Hourly Continuation — ONDO/USDT P34_50

**Symbol:** ONDO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 902 |
| net_profit_factor | 0.4090 |
| net_win_rate | 0.4235 |
| gross_profit_factor | 0.8274 |
| gross_win_rate | 0.4390 |
| sharpe_ratio | -8.9085 |
| sortino_ratio | -3.7965 |
| max_drawdown | 0.9918 |
| cagr | -0.8523 |
| net_avg_win | 17.9670 |
| net_avg_loss | -32.2717 |
| avg_hold_time_bars | 2.5743 |
| exposure | 0.1055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
