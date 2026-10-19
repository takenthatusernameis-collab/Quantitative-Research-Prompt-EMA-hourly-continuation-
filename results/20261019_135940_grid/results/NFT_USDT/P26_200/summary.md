# EMA Hourly Continuation — NFT/USDT P26_200

**Symbol:** NFT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 713 |
| net_profit_factor | 0.2741 |
| net_win_rate | 0.2693 |
| gross_profit_factor | 0.6131 |
| gross_win_rate | 0.3043 |
| sharpe_ratio | -13.1649 |
| sortino_ratio | -5.2239 |
| max_drawdown | 0.9992 |
| cagr | -0.9403 |
| net_avg_win | 19.6459 |
| net_avg_loss | -26.4176 |
| avg_hold_time_bars | 17.6914 |
| exposure | 0.5734 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
