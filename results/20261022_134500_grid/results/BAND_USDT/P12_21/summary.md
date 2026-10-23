# EMA Hourly Continuation — BAND/USDT P12_21

**Symbol:** BAND/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1301 |
| net_profit_factor | 0.3259 |
| net_win_rate | 0.4243 |
| gross_profit_factor | 0.8486 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -11.0723 |
| sortino_ratio | -5.6570 |
| max_drawdown | 0.9993 |
| cagr | -0.9424 |
| net_avg_win | 8.7532 |
| net_avg_loss | -19.7921 |
| avg_hold_time_bars | 3.0945 |
| exposure | 0.1822 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
