# EMA Hourly Continuation — FLOKI/USDT P89_200

**Symbol:** FLOKI/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 226 |
| net_profit_factor | 0.7911 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9815 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.0316 |
| sortino_ratio | -0.2220 |
| max_drawdown | 0.2284 |
| cagr | -0.0981 |
| net_avg_win | 76.5593 |
| net_avg_loss | -96.7725 |
| avg_hold_time_bars | 20.5088 |
| exposure | 0.2107 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
