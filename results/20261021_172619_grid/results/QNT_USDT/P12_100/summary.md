# EMA Hourly Continuation — QNT/USDT P12_100

**Symbol:** QNT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 595 |
| net_profit_factor | 0.8011 |
| net_win_rate | 0.5126 |
| gross_profit_factor | 1.0432 |
| gross_win_rate | 0.5126 |
| sharpe_ratio | -1.6503 |
| sortino_ratio | -0.5785 |
| max_drawdown | 0.5132 |
| cagr | -0.2340 |
| net_avg_win | 64.4389 |
| net_avg_loss | -84.5973 |
| avg_hold_time_bars | 17.8824 |
| exposure | 0.4836 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
