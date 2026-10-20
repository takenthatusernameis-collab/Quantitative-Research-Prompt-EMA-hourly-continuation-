# EMA Hourly Continuation — AVA/USDT P50_200

**Symbol:** AVA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.6666 |
| net_win_rate | 0.4973 |
| gross_profit_factor | 0.9578 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.0898 |
| sortino_ratio | -0.5658 |
| max_drawdown | 0.5574 |
| cagr | -0.2359 |
| net_avg_win | 53.9693 |
| net_avg_loss | -80.0821 |
| avg_hold_time_bars | 22.6421 |
| exposure | 0.3767 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
