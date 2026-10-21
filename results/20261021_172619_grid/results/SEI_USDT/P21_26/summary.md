# EMA Hourly Continuation — SEI/USDT P21_26

**Symbol:** SEI/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 160 |
| net_profit_factor | 0.6769 |
| net_win_rate | 0.4813 |
| gross_profit_factor | 0.9396 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -1.6034 |
| sortino_ratio | -0.2903 |
| max_drawdown | 0.3178 |
| cagr | -0.1248 |
| net_avg_win | 77.3880 |
| net_avg_loss | -106.0628 |
| avg_hold_time_bars | 4.7375 |
| exposure | 0.0345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
