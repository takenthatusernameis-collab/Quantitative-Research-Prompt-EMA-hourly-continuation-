# EMA Hourly Continuation — XMR/USDT P20_34

**Symbol:** XMR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1529 |
| net_profit_factor | 0.1235 |
| net_win_rate | 0.3578 |
| gross_profit_factor | 0.4530 |
| gross_win_rate | 0.3833 |
| sharpe_ratio | -16.5426 |
| sortino_ratio | -9.3533 |
| max_drawdown | 1.0000 |
| cagr | -0.9931 |
| net_avg_win | 2.5751 |
| net_avg_loss | -11.6177 |
| avg_hold_time_bars | 1.9686 |
| exposure | 0.1368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
