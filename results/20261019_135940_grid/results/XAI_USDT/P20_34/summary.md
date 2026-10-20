# EMA Hourly Continuation — XAI/USDT P20_34

**Symbol:** XAI/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1237 |
| net_profit_factor | 0.4923 |
| net_win_rate | 0.3945 |
| gross_profit_factor | 0.8737 |
| gross_win_rate | 0.4228 |
| sharpe_ratio | -10.8997 |
| sortino_ratio | -5.4340 |
| max_drawdown | 0.9989 |
| cagr | -0.9328 |
| net_avg_win | 19.8453 |
| net_avg_loss | -26.2659 |
| avg_hold_time_bars | 3.0647 |
| exposure | 0.1723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
