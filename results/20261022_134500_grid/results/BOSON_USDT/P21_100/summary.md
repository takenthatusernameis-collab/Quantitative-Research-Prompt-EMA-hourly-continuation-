# EMA Hourly Continuation — BOSON/USDT P21_100

**Symbol:** BOSON/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.6776 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.9191 |
| gross_win_rate | 0.4673 |
| sharpe_ratio | -3.4557 |
| sortino_ratio | -1.2485 |
| max_drawdown | 0.7712 |
| cagr | -0.4434 |
| net_avg_win | 52.9039 |
| net_avg_loss | -68.0689 |
| avg_hold_time_bars | 13.6910 |
| exposure | 0.4089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
