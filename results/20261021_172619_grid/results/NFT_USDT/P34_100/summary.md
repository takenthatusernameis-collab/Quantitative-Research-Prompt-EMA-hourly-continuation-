# EMA Hourly Continuation — NFT/USDT P34_100

**Symbol:** NFT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.4147 |
| net_win_rate | 0.3607 |
| gross_profit_factor | 0.7241 |
| gross_win_rate | 0.3607 |
| sharpe_ratio | -6.8261 |
| sortino_ratio | -1.9816 |
| max_drawdown | 0.9135 |
| cagr | -0.6104 |
| net_avg_win | 44.2839 |
| net_avg_loss | -60.2475 |
| avg_hold_time_bars | 16.4652 |
| exposure | 0.3009 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
