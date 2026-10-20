# EMA Hourly Continuation — TFUEL/USDT P55_200

**Symbol:** TFUEL/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.4773 |
| net_win_rate | 0.3907 |
| gross_profit_factor | 0.7411 |
| gross_win_rate | 0.4043 |
| sharpe_ratio | -5.9176 |
| sortino_ratio | -1.8850 |
| max_drawdown | 0.9043 |
| cagr | -0.6026 |
| net_avg_win | 40.7912 |
| net_avg_loss | -54.8080 |
| avg_hold_time_bars | 14.3056 |
| exposure | 0.3347 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
