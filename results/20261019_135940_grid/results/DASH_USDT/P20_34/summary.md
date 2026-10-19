# EMA Hourly Continuation — DASH/USDT P20_34

**Symbol:** DASH/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1180 |
| net_profit_factor | 0.2108 |
| net_win_rate | 0.3992 |
| gross_profit_factor | 0.7089 |
| gross_win_rate | 0.4331 |
| sharpe_ratio | -11.9803 |
| sortino_ratio | -5.8550 |
| max_drawdown | 0.9995 |
| cagr | -0.9530 |
| net_avg_win | 5.6680 |
| net_avg_loss | -17.8632 |
| avg_hold_time_bars | 2.6534 |
| exposure | 0.1423 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
