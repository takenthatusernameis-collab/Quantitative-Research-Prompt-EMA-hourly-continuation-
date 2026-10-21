# EMA Hourly Continuation — NFT/USDT P21_50

**Symbol:** NFT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.3047 |
| net_win_rate | 0.2840 |
| gross_profit_factor | 0.5655 |
| gross_win_rate | 0.2981 |
| sharpe_ratio | -8.8929 |
| sortino_ratio | -2.7071 |
| max_drawdown | 0.9618 |
| cagr | -0.7276 |
| net_avg_win | 34.8363 |
| net_avg_loss | -45.3560 |
| avg_hold_time_bars | 9.3427 |
| exposure | 0.1809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
