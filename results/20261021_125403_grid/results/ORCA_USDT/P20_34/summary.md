# EMA Hourly Continuation — ORCA/USDT P20_34

**Symbol:** ORCA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.6143 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 0.9392 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -3.3801 |
| sortino_ratio | -1.0253 |
| max_drawdown | 0.7130 |
| cagr | -0.3786 |
| net_avg_win | 51.6516 |
| net_avg_loss | -76.9275 |
| avg_hold_time_bars | 5.7378 |
| exposure | 0.1174 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
