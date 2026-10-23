# EMA Hourly Continuation — YGG/USDT P100_144

**Symbol:** YGG/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.5634 |
| net_win_rate | 0.4861 |
| gross_profit_factor | 0.9441 |
| gross_win_rate | 0.4904 |
| sharpe_ratio | -3.9087 |
| sortino_ratio | -1.1914 |
| max_drawdown | 0.7723 |
| cagr | -0.4380 |
| net_avg_win | 43.5597 |
| net_avg_loss | -73.1301 |
| avg_hold_time_bars | 4.2206 |
| exposure | 0.0892 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
