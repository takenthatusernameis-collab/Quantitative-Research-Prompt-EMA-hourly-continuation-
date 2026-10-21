# EMA Hourly Continuation — XYO/USDT P8_50

**Symbol:** XYO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 753 |
| net_profit_factor | 0.6152 |
| net_win_rate | 0.4409 |
| gross_profit_factor | 0.8089 |
| gross_win_rate | 0.4422 |
| sharpe_ratio | -4.5356 |
| sortino_ratio | -1.7621 |
| max_drawdown | 0.8723 |
| cagr | -0.5556 |
| net_avg_win | 41.9342 |
| net_avg_loss | -53.7526 |
| avg_hold_time_bars | 11.2882 |
| exposure | 0.3846 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
