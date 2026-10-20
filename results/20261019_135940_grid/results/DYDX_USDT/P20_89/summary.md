# EMA Hourly Continuation — DYDX/USDT P20_89

**Symbol:** DYDX/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 695 |
| net_profit_factor | 0.6545 |
| net_win_rate | 0.4835 |
| gross_profit_factor | 0.9829 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -3.6735 |
| sortino_ratio | -1.3670 |
| max_drawdown | 0.8075 |
| cagr | -0.4751 |
| net_avg_win | 45.2138 |
| net_avg_loss | -64.6523 |
| avg_hold_time_bars | 13.0849 |
| exposure | 0.4134 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
