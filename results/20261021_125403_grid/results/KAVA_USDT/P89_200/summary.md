# EMA Hourly Continuation — KAVA/USDT P89_200

**Symbol:** KAVA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.7228 |
| net_win_rate | 0.5069 |
| gross_profit_factor | 1.0525 |
| gross_win_rate | 0.5138 |
| sharpe_ratio | -1.8489 |
| sortino_ratio | -0.4454 |
| max_drawdown | 0.4617 |
| cagr | -0.1913 |
| net_avg_win | 73.3041 |
| net_avg_loss | -104.2554 |
| avg_hold_time_bars | 15.9690 |
| exposure | 0.2105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
