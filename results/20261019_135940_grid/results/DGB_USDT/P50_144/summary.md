# EMA Hourly Continuation — DGB/USDT P50_144

**Symbol:** DGB/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 548 |
| net_profit_factor | 0.5583 |
| net_win_rate | 0.4526 |
| gross_profit_factor | 0.8601 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -4.4804 |
| sortino_ratio | -1.4790 |
| max_drawdown | 0.8350 |
| cagr | -0.5068 |
| net_avg_win | 42.3224 |
| net_avg_loss | -62.6718 |
| avg_hold_time_bars | 12.1332 |
| exposure | 0.3022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
