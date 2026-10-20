# EMA Hourly Continuation — MOG/USDT P21_34

**Symbol:** MOG/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1036 |
| net_profit_factor | 0.5079 |
| net_win_rate | 0.4266 |
| gross_profit_factor | 0.8071 |
| gross_win_rate | 0.4421 |
| sharpe_ratio | -8.8394 |
| sortino_ratio | -4.1818 |
| max_drawdown | 0.9916 |
| cagr | -0.8751 |
| net_avg_win | 23.1540 |
| net_avg_loss | -33.9223 |
| avg_hold_time_bars | 2.8340 |
| exposure | 0.1460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
