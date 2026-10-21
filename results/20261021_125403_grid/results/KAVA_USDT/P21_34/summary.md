# EMA Hourly Continuation — KAVA/USDT P21_34

**Symbol:** KAVA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.5501 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.9340 |
| gross_win_rate | 0.4704 |
| sharpe_ratio | -4.1341 |
| sortino_ratio | -1.1692 |
| max_drawdown | 0.7542 |
| cagr | -0.4221 |
| net_avg_win | 50.7894 |
| net_avg_loss | -79.5148 |
| avg_hold_time_bars | 6.2494 |
| exposure | 0.1105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
