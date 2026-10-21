# EMA Hourly Continuation — EUL/USDT P12_50

**Symbol:** EUL/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.7114 |
| net_win_rate | 0.4856 |
| gross_profit_factor | 0.9055 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -2.3401 |
| sortino_ratio | -0.8362 |
| max_drawdown | 0.6340 |
| cagr | -0.3186 |
| net_avg_win | 50.1352 |
| net_avg_loss | -66.5380 |
| avg_hold_time_bars | 11.4537 |
| exposure | 0.3259 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
