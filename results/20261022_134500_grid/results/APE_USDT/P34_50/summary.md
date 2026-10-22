# EMA Hourly Continuation — APE/USDT P34_50

**Symbol:** APE/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 950 |
| net_profit_factor | 0.4087 |
| net_win_rate | 0.4463 |
| gross_profit_factor | 0.9400 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -8.7556 |
| sortino_ratio | -3.8299 |
| max_drawdown | 0.9919 |
| cagr | -0.8525 |
| net_avg_win | 16.1680 |
| net_avg_loss | -31.8888 |
| avg_hold_time_bars | 2.4074 |
| exposure | 0.1040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
