# EMA Hourly Continuation — FLOKI/USDT P20_21

**Symbol:** FLOKI/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 140 |
| net_profit_factor | 0.5171 |
| net_win_rate | 0.4071 |
| gross_profit_factor | 0.7085 |
| gross_win_rate | 0.4071 |
| sharpe_ratio | -2.5495 |
| sortino_ratio | -0.4291 |
| max_drawdown | 0.4038 |
| cagr | -0.1803 |
| net_avg_win | 73.8397 |
| net_avg_loss | -98.0597 |
| avg_hold_time_bars | 5.4929 |
| exposure | 0.0350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
