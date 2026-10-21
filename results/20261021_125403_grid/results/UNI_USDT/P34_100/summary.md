# EMA Hourly Continuation — UNI/USDT P34_100

**Symbol:** UNI/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.8291 |
| net_win_rate | 0.5155 |
| gross_profit_factor | 1.0501 |
| gross_win_rate | 0.5155 |
| sharpe_ratio | -1.0674 |
| sortino_ratio | -0.3016 |
| max_drawdown | 0.3186 |
| cagr | -0.1309 |
| net_avg_win | 72.3750 |
| net_avg_loss | -92.8949 |
| avg_hold_time_bars | 14.1244 |
| exposure | 0.2478 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
