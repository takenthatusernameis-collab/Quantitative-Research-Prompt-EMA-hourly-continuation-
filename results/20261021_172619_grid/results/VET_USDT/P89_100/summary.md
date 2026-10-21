# EMA Hourly Continuation — VET/USDT P89_100

**Symbol:** VET/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 100 |
| net_profit_factor | 0.7580 |
| net_win_rate | 0.5300 |
| gross_profit_factor | 1.1221 |
| gross_win_rate | 0.5300 |
| sharpe_ratio | -0.8459 |
| sortino_ratio | -0.1222 |
| max_drawdown | 0.1753 |
| cagr | -0.0546 |
| net_avg_win | 77.7271 |
| net_avg_loss | -115.6361 |
| avg_hold_time_bars | 4.9800 |
| exposure | 0.0226 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
