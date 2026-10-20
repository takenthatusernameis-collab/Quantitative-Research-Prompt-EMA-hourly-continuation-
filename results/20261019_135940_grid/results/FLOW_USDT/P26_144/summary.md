# EMA Hourly Continuation — FLOW/USDT P26_144

**Symbol:** FLOW/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.5745 |
| net_win_rate | 0.4561 |
| gross_profit_factor | 0.9116 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -3.8845 |
| sortino_ratio | -1.1885 |
| max_drawdown | 0.7741 |
| cagr | -0.4382 |
| net_avg_win | 47.3867 |
| net_avg_loss | -69.1547 |
| avg_hold_time_bars | 23.6925 |
| exposure | 0.5148 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
