# EMA Hourly Continuation — RENDER/USDT P89_200

**Symbol:** RENDER/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 218 |
| net_profit_factor | 0.9020 |
| net_win_rate | 0.5275 |
| gross_profit_factor | 1.1063 |
| gross_win_rate | 0.5275 |
| sharpe_ratio | -0.4775 |
| sortino_ratio | -0.1096 |
| max_drawdown | 0.2139 |
| cagr | -0.0518 |
| net_avg_win | 86.9870 |
| net_avg_loss | -107.6716 |
| avg_hold_time_bars | 18.3670 |
| exposure | 0.2113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
