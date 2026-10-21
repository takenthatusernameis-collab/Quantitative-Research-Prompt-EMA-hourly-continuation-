# EMA Hourly Continuation — KMNO/USDT P8_34

**Symbol:** KMNO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 705 |
| net_profit_factor | 0.7803 |
| net_win_rate | 0.5035 |
| gross_profit_factor | 1.0096 |
| gross_win_rate | 0.5050 |
| sharpe_ratio | -2.0965 |
| sortino_ratio | -0.8036 |
| max_drawdown | 0.6095 |
| cagr | -0.3108 |
| net_avg_win | 60.1949 |
| net_avg_loss | -78.2437 |
| avg_hold_time_bars | 8.7333 |
| exposure | 0.2843 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
