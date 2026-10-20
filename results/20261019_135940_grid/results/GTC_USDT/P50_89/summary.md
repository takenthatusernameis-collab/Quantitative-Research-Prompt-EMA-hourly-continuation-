# EMA Hourly Continuation — GTC/USDT P50_89

**Symbol:** GTC/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.5865 |
| net_win_rate | 0.4768 |
| gross_profit_factor | 1.0050 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -4.5474 |
| sortino_ratio | -1.6661 |
| max_drawdown | 0.8752 |
| cagr | -0.5455 |
| net_avg_win | 38.4507 |
| net_avg_loss | -59.7344 |
| avg_hold_time_bars | 5.6012 |
| exposure | 0.1698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
