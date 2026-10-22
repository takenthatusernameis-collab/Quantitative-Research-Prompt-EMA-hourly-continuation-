# EMA Hourly Continuation — RIO/USDT P8_12

**Symbol:** RIO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 196 |
| net_profit_factor | 0.6236 |
| net_win_rate | 0.4184 |
| gross_profit_factor | 0.7535 |
| gross_win_rate | 0.4184 |
| sharpe_ratio | -2.2742 |
| sortino_ratio | -0.4517 |
| max_drawdown | 0.4157 |
| cagr | -0.1883 |
| net_avg_win | 81.7593 |
| net_avg_loss | -94.3072 |
| avg_hold_time_bars | 5.0663 |
| exposure | 0.0456 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
