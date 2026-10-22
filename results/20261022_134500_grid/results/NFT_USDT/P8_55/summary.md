# EMA Hourly Continuation — NFT/USDT P8_55

**Symbol:** NFT/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1556 |
| net_profit_factor | 0.2049 |
| net_win_rate | 0.2436 |
| gross_profit_factor | 0.5754 |
| gross_win_rate | 0.2905 |
| sharpe_ratio | -21.7298 |
| sortino_ratio | -12.9964 |
| max_drawdown | 1.0000 |
| cagr | -0.9992 |
| net_avg_win | 6.7982 |
| net_avg_loss | -10.6852 |
| avg_hold_time_bars | 6.7449 |
| exposure | 0.4770 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
