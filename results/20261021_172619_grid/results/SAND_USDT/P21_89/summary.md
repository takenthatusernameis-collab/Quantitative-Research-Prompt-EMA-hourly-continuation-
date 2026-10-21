# EMA Hourly Continuation — SAND/USDT P21_89

**Symbol:** SAND/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.6584 |
| net_win_rate | 0.4511 |
| gross_profit_factor | 0.8516 |
| gross_win_rate | 0.4511 |
| sharpe_ratio | -3.0922 |
| sortino_ratio | -0.9524 |
| max_drawdown | 0.6917 |
| cagr | -0.3549 |
| net_avg_win | 60.6654 |
| net_avg_loss | -75.7159 |
| avg_hold_time_bars | 17.0298 |
| exposure | 0.3638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
