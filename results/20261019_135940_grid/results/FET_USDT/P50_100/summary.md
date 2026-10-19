# EMA Hourly Continuation — FET/USDT P50_100

**Symbol:** FET/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.5874 |
| net_win_rate | 0.4819 |
| gross_profit_factor | 0.9403 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -3.8787 |
| sortino_ratio | -1.3098 |
| max_drawdown | 0.8049 |
| cagr | -0.4689 |
| net_avg_win | 40.4749 |
| net_avg_loss | -64.0940 |
| avg_hold_time_bars | 6.4492 |
| exposure | 0.1703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
