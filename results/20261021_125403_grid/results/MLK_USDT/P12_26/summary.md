# EMA Hourly Continuation — MLK/USDT P12_26

**Symbol:** MLK/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.3131 |
| net_win_rate | 0.3044 |
| gross_profit_factor | 0.5301 |
| gross_win_rate | 0.3138 |
| sharpe_ratio | -7.5025 |
| sortino_ratio | -2.2057 |
| max_drawdown | 0.9301 |
| cagr | -0.6500 |
| net_avg_win | 32.5836 |
| net_avg_loss | -45.5490 |
| avg_hold_time_bars | 6.6838 |
| exposure | 0.1292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
