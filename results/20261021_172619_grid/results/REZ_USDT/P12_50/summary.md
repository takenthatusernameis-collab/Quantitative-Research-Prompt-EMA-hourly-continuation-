# EMA Hourly Continuation — REZ/USDT P12_50

**Symbol:** REZ/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.8156 |
| net_win_rate | 0.4961 |
| gross_profit_factor | 1.0000 |
| gross_win_rate | 0.4961 |
| sharpe_ratio | -1.8637 |
| sortino_ratio | -0.6843 |
| max_drawdown | 0.5926 |
| cagr | -0.2714 |
| net_avg_win | 74.6010 |
| net_avg_loss | -90.0684 |
| avg_hold_time_bars | 11.3220 |
| exposure | 0.3390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
