# EMA Hourly Continuation — POKT/USDT P8_89

**Symbol:** POKT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 918 |
| net_profit_factor | 0.5819 |
| net_win_rate | 0.4052 |
| gross_profit_factor | 0.8758 |
| gross_win_rate | 0.4183 |
| sharpe_ratio | -6.8910 |
| sortino_ratio | -2.9185 |
| max_drawdown | 0.9727 |
| cagr | -0.7544 |
| net_avg_win | 36.3311 |
| net_avg_loss | -42.5374 |
| avg_hold_time_bars | 15.0436 |
| exposure | 0.6249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
