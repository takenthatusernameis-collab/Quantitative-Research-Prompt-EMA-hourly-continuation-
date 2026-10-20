# EMA Hourly Continuation — ILV/USDT P26_200

**Symbol:** ILV/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.8530 |
| net_win_rate | 0.5371 |
| gross_profit_factor | 1.1747 |
| gross_win_rate | 0.5429 |
| sharpe_ratio | -0.8649 |
| sortino_ratio | -0.2295 |
| max_drawdown | 0.3177 |
| cagr | -0.1056 |
| net_avg_win | 75.4453 |
| net_avg_loss | -102.6428 |
| avg_hold_time_bars | 37.4800 |
| exposure | 0.5963 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
