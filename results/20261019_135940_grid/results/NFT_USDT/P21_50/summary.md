# EMA Hourly Continuation — NFT/USDT P21_50

**Symbol:** NFT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1566 |
| net_profit_factor | 0.1675 |
| net_win_rate | 0.1986 |
| gross_profit_factor | 0.5332 |
| gross_win_rate | 0.2676 |
| sharpe_ratio | -24.0630 |
| sortino_ratio | -14.9656 |
| max_drawdown | 1.0000 |
| cagr | -0.9998 |
| net_avg_win | 6.4715 |
| net_avg_loss | -9.5718 |
| avg_hold_time_bars | 3.7848 |
| exposure | 0.2694 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
