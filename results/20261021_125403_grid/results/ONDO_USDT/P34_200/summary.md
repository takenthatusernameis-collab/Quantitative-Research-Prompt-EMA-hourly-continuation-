# EMA Hourly Continuation — ONDO/USDT P34_200

**Symbol:** ONDO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.7439 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.8804 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -1.6684 |
| sortino_ratio | -0.4206 |
| max_drawdown | 0.4009 |
| cagr | -0.1762 |
| net_avg_win | 76.1764 |
| net_avg_loss | -89.5972 |
| avg_hold_time_bars | 28.6190 |
| exposure | 0.4098 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
