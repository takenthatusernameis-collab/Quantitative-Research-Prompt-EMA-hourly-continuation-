# EMA Hourly Continuation — KMNO/USDT P21_144

**Symbol:** KMNO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.8769 |
| net_win_rate | 0.5145 |
| gross_profit_factor | 1.0603 |
| gross_win_rate | 0.5145 |
| sharpe_ratio | -0.7708 |
| sortino_ratio | -0.2072 |
| max_drawdown | 0.2661 |
| cagr | -0.0941 |
| net_avg_win | 86.7318 |
| net_avg_loss | -104.7949 |
| avg_hold_time_bars | 32.1445 |
| exposure | 0.5135 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
