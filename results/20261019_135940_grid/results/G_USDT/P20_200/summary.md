# EMA Hourly Continuation — G/USDT P20_200

**Symbol:** G/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.5510 |
| net_win_rate | 0.4399 |
| gross_profit_factor | 0.7689 |
| gross_win_rate | 0.4430 |
| sharpe_ratio | -3.4201 |
| sortino_ratio | -0.9233 |
| max_drawdown | 0.6440 |
| cagr | -0.3487 |
| net_avg_win | 53.4812 |
| net_avg_loss | -76.2261 |
| avg_hold_time_bars | 40.5918 |
| exposure | 0.6745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
