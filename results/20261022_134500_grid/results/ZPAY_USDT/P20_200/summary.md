# EMA Hourly Continuation — ZPAY/USDT P20_200

**Symbol:** ZPAY/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.6217 |
| net_win_rate | 0.4214 |
| gross_profit_factor | 0.7306 |
| gross_win_rate | 0.4214 |
| sharpe_ratio | -2.5505 |
| sortino_ratio | -0.6183 |
| max_drawdown | 0.5316 |
| cagr | -0.2491 |
| net_avg_win | 67.1290 |
| net_avg_loss | -78.6358 |
| avg_hold_time_bars | 52.6020 |
| exposure | 0.7117 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
