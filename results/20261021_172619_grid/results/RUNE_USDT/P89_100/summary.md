# EMA Hourly Continuation — RUNE/USDT P89_100

**Symbol:** RUNE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 98 |
| net_profit_factor | 0.8972 |
| net_win_rate | 0.5714 |
| gross_profit_factor | 1.3183 |
| gross_win_rate | 0.5714 |
| sharpe_ratio | -0.2965 |
| sortino_ratio | -0.0429 |
| max_drawdown | 0.1035 |
| cagr | -0.0201 |
| net_avg_win | 77.5151 |
| net_avg_loss | -115.1991 |
| avg_hold_time_bars | 5.5816 |
| exposure | 0.0249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
