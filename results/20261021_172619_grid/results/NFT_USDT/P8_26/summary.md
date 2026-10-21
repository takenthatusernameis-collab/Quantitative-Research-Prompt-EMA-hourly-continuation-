# EMA Hourly Continuation — NFT/USDT P8_26

**Symbol:** NFT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.3052 |
| net_win_rate | 0.2720 |
| gross_profit_factor | 0.5484 |
| gross_win_rate | 0.2759 |
| sharpe_ratio | -10.1819 |
| sortino_ratio | -3.3975 |
| max_drawdown | 0.9848 |
| cagr | -0.8107 |
| net_avg_win | 31.1149 |
| net_avg_loss | -38.0965 |
| avg_hold_time_bars | 7.5636 |
| exposure | 0.1757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
