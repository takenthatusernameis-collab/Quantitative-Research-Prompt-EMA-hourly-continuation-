# EMA Hourly Continuation — AUCTION/USDT P20_100

**Symbol:** AUCTION/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.5765 |
| net_win_rate | 0.4495 |
| gross_profit_factor | 0.8758 |
| gross_win_rate | 0.4721 |
| sharpe_ratio | -4.7840 |
| sortino_ratio | -1.7325 |
| max_drawdown | 0.8809 |
| cagr | -0.5611 |
| net_avg_win | 39.9605 |
| net_avg_loss | -56.5893 |
| avg_hold_time_bars | 14.8220 |
| exposure | 0.4448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
