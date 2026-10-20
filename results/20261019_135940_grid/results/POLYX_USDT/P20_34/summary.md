# EMA Hourly Continuation — POLYX/USDT P20_34

**Symbol:** POLYX/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1064 |
| net_profit_factor | 0.4208 |
| net_win_rate | 0.4370 |
| gross_profit_factor | 0.8888 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -9.3298 |
| sortino_ratio | -4.3278 |
| max_drawdown | 0.9956 |
| cagr | -0.8840 |
| net_avg_win | 15.5531 |
| net_avg_loss | -28.6935 |
| avg_hold_time_bars | 3.3647 |
| exposure | 0.1627 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
