# EMA Hourly Continuation — GTC/USDT P50_144

**Symbol:** GTC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.5914 |
| net_win_rate | 0.4611 |
| gross_profit_factor | 0.8739 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -3.4133 |
| sortino_ratio | -1.0490 |
| max_drawdown | 0.7283 |
| cagr | -0.3897 |
| net_avg_win | 46.9721 |
| net_avg_loss | -67.9440 |
| avg_hold_time_bars | 14.5453 |
| exposure | 0.3140 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
