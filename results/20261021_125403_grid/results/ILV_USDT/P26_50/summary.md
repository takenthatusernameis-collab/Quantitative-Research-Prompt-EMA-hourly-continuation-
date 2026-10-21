# EMA Hourly Continuation — ILV/USDT P26_50

**Symbol:** ILV/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.7271 |
| net_win_rate | 0.5022 |
| gross_profit_factor | 1.0066 |
| gross_win_rate | 0.5022 |
| sharpe_ratio | -2.1532 |
| sortino_ratio | -0.6532 |
| max_drawdown | 0.5502 |
| cagr | -0.2574 |
| net_avg_win | 62.5997 |
| net_avg_loss | -86.8766 |
| avg_hold_time_bars | 6.1076 |
| exposure | 0.1238 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
