# EMA Hourly Continuation — ETC/USDT P100_200

**Symbol:** ETC/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.5281 |
| net_win_rate | 0.4556 |
| gross_profit_factor | 0.9709 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -4.6590 |
| sortino_ratio | -1.3409 |
| max_drawdown | 0.8205 |
| cagr | -0.4831 |
| net_avg_win | 47.6718 |
| net_avg_loss | -75.5553 |
| avg_hold_time_bars | 8.4101 |
| exposure | 0.1594 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
