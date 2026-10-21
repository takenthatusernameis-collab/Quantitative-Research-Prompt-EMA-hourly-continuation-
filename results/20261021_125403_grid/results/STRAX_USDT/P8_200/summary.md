# EMA Hourly Continuation — STRAX/USDT P8_200

**Symbol:** STRAX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.6708 |
| net_win_rate | 0.4506 |
| gross_profit_factor | 0.8390 |
| gross_win_rate | 0.4506 |
| sharpe_ratio | -2.9896 |
| sortino_ratio | -0.9365 |
| max_drawdown | 0.6599 |
| cagr | -0.3507 |
| net_avg_win | 61.4071 |
| net_avg_loss | -75.0816 |
| avg_hold_time_bars | 30.2366 |
| exposure | 0.6719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
