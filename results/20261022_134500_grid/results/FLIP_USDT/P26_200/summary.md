# EMA Hourly Continuation — FLIP/USDT P26_200

**Symbol:** FLIP/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.5367 |
| net_win_rate | 0.4291 |
| gross_profit_factor | 0.7419 |
| gross_win_rate | 0.4362 |
| sharpe_ratio | -3.0021 |
| sortino_ratio | -0.7027 |
| max_drawdown | 0.5892 |
| cagr | -0.2871 |
| net_avg_win | 54.8144 |
| net_avg_loss | -76.7602 |
| avg_hold_time_bars | 44.2872 |
| exposure | 0.5677 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
