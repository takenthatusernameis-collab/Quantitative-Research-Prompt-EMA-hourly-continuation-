# EMA Hourly Continuation — REQ/USDT P20_34

**Symbol:** REQ/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1260 |
| net_profit_factor | 0.3265 |
| net_win_rate | 0.3643 |
| gross_profit_factor | 0.8669 |
| gross_win_rate | 0.4270 |
| sharpe_ratio | -14.1771 |
| sortino_ratio | -7.3268 |
| max_drawdown | 0.9999 |
| cagr | -0.9771 |
| net_avg_win | 10.5598 |
| net_avg_loss | -18.5346 |
| avg_hold_time_bars | 3.3048 |
| exposure | 0.1893 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
