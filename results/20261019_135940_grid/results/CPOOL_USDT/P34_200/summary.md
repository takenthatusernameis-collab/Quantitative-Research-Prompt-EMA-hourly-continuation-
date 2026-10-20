# EMA Hourly Continuation — CPOOL/USDT P34_200

**Symbol:** CPOOL/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.5697 |
| net_win_rate | 0.4163 |
| gross_profit_factor | 0.7417 |
| gross_win_rate | 0.4163 |
| sharpe_ratio | -4.5369 |
| sortino_ratio | -1.4352 |
| max_drawdown | 0.8378 |
| cagr | -0.5030 |
| net_avg_win | 51.1815 |
| net_avg_loss | -64.0837 |
| avg_hold_time_bars | 16.6654 |
| exposure | 0.3894 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
