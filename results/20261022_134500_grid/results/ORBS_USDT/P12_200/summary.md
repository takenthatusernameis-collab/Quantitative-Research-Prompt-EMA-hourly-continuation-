# EMA Hourly Continuation — ORBS/USDT P12_200

**Symbol:** ORBS/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.5690 |
| net_win_rate | 0.4328 |
| gross_profit_factor | 0.8731 |
| gross_win_rate | 0.4457 |
| sharpe_ratio | -4.7360 |
| sortino_ratio | -1.5432 |
| max_drawdown | 0.8508 |
| cagr | -0.5274 |
| net_avg_win | 47.6216 |
| net_avg_loss | -63.8578 |
| avg_hold_time_bars | 27.8729 |
| exposure | 0.6880 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
