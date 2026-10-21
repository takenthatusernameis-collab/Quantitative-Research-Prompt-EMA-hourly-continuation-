# EMA Hourly Continuation — MANA/USDT P89_100

**Symbol:** MANA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 108 |
| net_profit_factor | 0.6967 |
| net_win_rate | 0.5093 |
| gross_profit_factor | 1.0386 |
| gross_win_rate | 0.5093 |
| sharpe_ratio | -1.1665 |
| sortino_ratio | -0.1746 |
| max_drawdown | 0.2100 |
| cagr | -0.0764 |
| net_avg_win | 75.5905 |
| net_avg_loss | -112.5935 |
| avg_hold_time_bars | 4.3519 |
| exposure | 0.0214 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
