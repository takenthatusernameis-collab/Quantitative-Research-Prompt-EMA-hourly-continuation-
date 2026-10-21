# EMA Hourly Continuation — GRT/USDT P26_55

**Symbol:** GRT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.7121 |
| net_win_rate | 0.4911 |
| gross_profit_factor | 0.9519 |
| gross_win_rate | 0.4911 |
| sharpe_ratio | -2.2372 |
| sortino_ratio | -0.6771 |
| max_drawdown | 0.5522 |
| cagr | -0.2659 |
| net_avg_win | 60.8933 |
| net_avg_loss | -82.5062 |
| avg_hold_time_bars | 6.6674 |
| exposure | 0.1352 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
