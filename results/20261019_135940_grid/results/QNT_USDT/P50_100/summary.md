# EMA Hourly Continuation — QNT/USDT P50_100

**Symbol:** QNT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 740 |
| net_profit_factor | 0.4197 |
| net_win_rate | 0.4459 |
| gross_profit_factor | 0.8133 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -6.9653 |
| sortino_ratio | -2.6581 |
| max_drawdown | 0.9664 |
| cagr | -0.7374 |
| net_avg_win | 21.1536 |
| net_avg_loss | -40.5676 |
| avg_hold_time_bars | 5.2054 |
| exposure | 0.1751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
