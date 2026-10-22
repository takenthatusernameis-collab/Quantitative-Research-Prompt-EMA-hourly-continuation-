# EMA Hourly Continuation — NFT/USDT P26_89

**Symbol:** NFT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1235 |
| net_profit_factor | 0.2736 |
| net_win_rate | 0.2316 |
| gross_profit_factor | 0.6736 |
| gross_win_rate | 0.2704 |
| sharpe_ratio | -19.7699 |
| sortino_ratio | -10.6557 |
| max_drawdown | 1.0000 |
| cagr | -0.9971 |
| net_avg_win | 13.1713 |
| net_avg_loss | -14.5068 |
| avg_hold_time_bars | 6.3263 |
| exposure | 0.3551 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
