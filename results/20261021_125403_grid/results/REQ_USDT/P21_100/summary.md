# EMA Hourly Continuation — REQ/USDT P21_100

**Symbol:** REQ/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.7072 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 0.9931 |
| gross_win_rate | 0.4874 |
| sharpe_ratio | -2.9040 |
| sortino_ratio | -0.9418 |
| max_drawdown | 0.6786 |
| cagr | -0.3522 |
| net_avg_win | 63.8675 |
| net_avg_loss | -85.8685 |
| avg_hold_time_bars | 16.4291 |
| exposure | 0.3846 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
