# EMA Hourly Continuation — GMT/USDT P12_50

**Symbol:** GMT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 645 |
| net_profit_factor | 0.7047 |
| net_win_rate | 0.4822 |
| gross_profit_factor | 0.9156 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -2.6514 |
| sortino_ratio | -0.9622 |
| max_drawdown | 0.6818 |
| cagr | -0.3564 |
| net_avg_win | 51.3667 |
| net_avg_loss | -67.8702 |
| avg_hold_time_bars | 10.6171 |
| exposure | 0.3113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
