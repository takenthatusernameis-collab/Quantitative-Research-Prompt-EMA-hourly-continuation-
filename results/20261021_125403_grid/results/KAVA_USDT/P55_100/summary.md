# EMA Hourly Continuation — KAVA/USDT P55_100

**Symbol:** KAVA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.6007 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.9173 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -3.5560 |
| sortino_ratio | -1.0029 |
| max_drawdown | 0.7115 |
| cagr | -0.3757 |
| net_avg_win | 57.0277 |
| net_avg_loss | -83.5261 |
| avg_hold_time_bars | 8.4629 |
| exposure | 0.1504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
