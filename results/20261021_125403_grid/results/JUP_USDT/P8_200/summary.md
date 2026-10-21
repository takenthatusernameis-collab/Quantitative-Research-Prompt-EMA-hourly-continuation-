# EMA Hourly Continuation — JUP/USDT P8_200

**Symbol:** JUP/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.7156 |
| net_win_rate | 0.4459 |
| gross_profit_factor | 0.8168 |
| gross_win_rate | 0.4490 |
| sharpe_ratio | -1.9236 |
| sortino_ratio | -0.4812 |
| max_drawdown | 0.4598 |
| cagr | -0.1997 |
| net_avg_win | 77.0234 |
| net_avg_loss | -86.6004 |
| avg_hold_time_bars | 52.5637 |
| exposure | 0.7502 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
