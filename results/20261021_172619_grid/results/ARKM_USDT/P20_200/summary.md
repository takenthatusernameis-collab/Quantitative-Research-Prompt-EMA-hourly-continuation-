# EMA Hourly Continuation — ARKM/USDT P20_200

**Symbol:** ARKM/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.8268 |
| net_win_rate | 0.4925 |
| gross_profit_factor | 0.9573 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -1.0530 |
| sortino_ratio | -0.2741 |
| max_drawdown | 0.3214 |
| cagr | -0.1202 |
| net_avg_win | 80.0315 |
| net_avg_loss | -93.9378 |
| avg_hold_time_bars | 40.4384 |
| exposure | 0.6121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
