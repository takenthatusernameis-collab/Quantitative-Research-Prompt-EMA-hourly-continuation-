# EMA Hourly Continuation — NFT/USDT P8_200

**Symbol:** NFT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.4920 |
| net_win_rate | 0.4029 |
| gross_profit_factor | 0.7469 |
| gross_win_rate | 0.4029 |
| sharpe_ratio | -5.1568 |
| sortino_ratio | -1.4844 |
| max_drawdown | 0.8300 |
| cagr | -0.5018 |
| net_avg_win | 48.7940 |
| net_avg_loss | -66.9308 |
| avg_hold_time_bars | 36.9017 |
| exposure | 0.6827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
