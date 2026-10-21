# EMA Hourly Continuation — DODO/USDT P21_89

**Symbol:** DODO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.7878 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9955 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -1.9378 |
| sortino_ratio | -0.6228 |
| max_drawdown | 0.5668 |
| cagr | -0.2492 |
| net_avg_win | 76.4163 |
| net_avg_loss | -93.9958 |
| avg_hold_time_bars | 16.0315 |
| exposure | 0.3685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
