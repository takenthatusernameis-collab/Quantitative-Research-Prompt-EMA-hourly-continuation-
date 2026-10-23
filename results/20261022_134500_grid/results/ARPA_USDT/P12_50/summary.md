# EMA Hourly Continuation — ARPA/USDT P12_50

**Symbol:** ARPA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1152 |
| net_profit_factor | 0.5332 |
| net_win_rate | 0.4375 |
| gross_profit_factor | 0.9029 |
| gross_win_rate | 0.4557 |
| sharpe_ratio | -8.0611 |
| sortino_ratio | -3.8395 |
| max_drawdown | 0.9914 |
| cagr | -0.8467 |
| net_avg_win | 22.4662 |
| net_avg_loss | -32.7697 |
| avg_hold_time_bars | 7.0443 |
| exposure | 0.3672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
