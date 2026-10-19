# EMA Hourly Continuation — TWT/USDT P8_89

**Symbol:** TWT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 788 |
| net_profit_factor | 0.5786 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 0.9627 |
| gross_win_rate | 0.5063 |
| sharpe_ratio | -4.1381 |
| sortino_ratio | -1.6357 |
| max_drawdown | 0.8768 |
| cagr | -0.5450 |
| net_avg_win | 30.4842 |
| net_avg_loss | -51.1087 |
| avg_hold_time_bars | 17.9289 |
| exposure | 0.6422 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
