# EMA Hourly Continuation — MOG/USDT P55_100

**Symbol:** MOG/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.6172 |
| net_win_rate | 0.4641 |
| gross_profit_factor | 0.8747 |
| gross_win_rate | 0.4676 |
| sharpe_ratio | -4.1581 |
| sortino_ratio | -1.4688 |
| max_drawdown | 0.8011 |
| cagr | -0.5000 |
| net_avg_win | 48.4643 |
| net_avg_loss | -67.9966 |
| avg_hold_time_bars | 4.8144 |
| exposure | 0.1367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
