# EMA Hourly Continuation — NFT/USDT P50_200

**Symbol:** NFT/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 819 |
| net_profit_factor | 0.3071 |
| net_win_rate | 0.2503 |
| gross_profit_factor | 0.7030 |
| gross_win_rate | 0.2882 |
| sharpe_ratio | -14.8201 |
| sortino_ratio | -6.3929 |
| max_drawdown | 0.9998 |
| cagr | -0.9674 |
| net_avg_win | 21.6179 |
| net_avg_loss | -23.5013 |
| avg_hold_time_bars | 10.7534 |
| exposure | 0.4003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
