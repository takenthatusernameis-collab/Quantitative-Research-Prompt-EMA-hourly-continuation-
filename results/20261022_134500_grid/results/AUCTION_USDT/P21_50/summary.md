# EMA Hourly Continuation — AUCTION/USDT P21_50

**Symbol:** AUCTION/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 947 |
| net_profit_factor | 0.4340 |
| net_win_rate | 0.4171 |
| gross_profit_factor | 0.7914 |
| gross_win_rate | 0.4435 |
| sharpe_ratio | -8.6461 |
| sortino_ratio | -3.7522 |
| max_drawdown | 0.9908 |
| cagr | -0.8433 |
| net_avg_win | 19.2321 |
| net_avg_loss | -31.7090 |
| avg_hold_time_bars | 5.5977 |
| exposure | 0.2399 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
