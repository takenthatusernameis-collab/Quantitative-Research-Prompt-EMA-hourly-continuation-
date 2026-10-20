# EMA Hourly Continuation — TURBO/USDT P8_20

**Symbol:** TURBO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1429 |
| net_profit_factor | 0.4670 |
| net_win_rate | 0.4115 |
| gross_profit_factor | 0.7968 |
| gross_win_rate | 0.4367 |
| sharpe_ratio | -11.9357 |
| sortino_ratio | -6.9544 |
| max_drawdown | 0.9993 |
| cagr | -0.9696 |
| net_avg_win | 14.8939 |
| net_avg_loss | -22.2960 |
| avg_hold_time_bars | 2.8202 |
| exposure | 0.2199 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
