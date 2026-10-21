# EMA Hourly Continuation — JST/USDT P8_100

**Symbol:** JST/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.7576 |
| net_win_rate | 0.5231 |
| gross_profit_factor | 1.0870 |
| gross_win_rate | 0.5255 |
| sharpe_ratio | -1.6208 |
| sortino_ratio | -0.4703 |
| max_drawdown | 0.4507 |
| cagr | -0.1950 |
| net_avg_win | 61.2606 |
| net_avg_loss | -88.7046 |
| avg_hold_time_bars | 36.8637 |
| exposure | 0.6856 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
