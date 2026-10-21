# EMA Hourly Continuation — XYO/USDT P20_89

**Symbol:** XYO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.6316 |
| net_win_rate | 0.4436 |
| gross_profit_factor | 0.8345 |
| gross_win_rate | 0.4436 |
| sharpe_ratio | -3.6873 |
| sortino_ratio | -1.1842 |
| max_drawdown | 0.7584 |
| cagr | -0.4209 |
| net_avg_win | 56.2527 |
| net_avg_loss | -70.9976 |
| avg_hold_time_bars | 16.1304 |
| exposure | 0.3752 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
