# EMA Hourly Continuation — TAO/USDT P50_100

**Symbol:** TAO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.8981 |
| net_win_rate | 0.5285 |
| gross_profit_factor | 1.1088 |
| gross_win_rate | 0.5285 |
| sharpe_ratio | -0.5429 |
| sortino_ratio | -0.1393 |
| max_drawdown | 0.1834 |
| cagr | -0.0652 |
| net_avg_win | 82.2832 |
| net_avg_loss | -102.6816 |
| avg_hold_time_bars | 9.3861 |
| exposure | 0.1348 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
