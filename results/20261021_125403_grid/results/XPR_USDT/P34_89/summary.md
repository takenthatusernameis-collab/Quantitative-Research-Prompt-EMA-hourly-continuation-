# EMA Hourly Continuation — XPR/USDT P34_89

**Symbol:** XPR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.7135 |
| net_win_rate | 0.4858 |
| gross_profit_factor | 0.9386 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -1.9042 |
| sortino_ratio | -0.4842 |
| max_drawdown | 0.4493 |
| cagr | -0.1991 |
| net_avg_win | 69.1024 |
| net_avg_loss | -91.5026 |
| avg_hold_time_bars | 10.8864 |
| exposure | 0.1569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
