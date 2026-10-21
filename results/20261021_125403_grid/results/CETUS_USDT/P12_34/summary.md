# EMA Hourly Continuation — CETUS/USDT P12_34

**Symbol:** CETUS/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.7610 |
| net_win_rate | 0.4837 |
| gross_profit_factor | 0.9828 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -2.6814 |
| sortino_ratio | -0.9935 |
| max_drawdown | 0.7081 |
| cagr | -0.3669 |
| net_avg_win | 66.6570 |
| net_avg_loss | -82.0645 |
| avg_hold_time_bars | 7.0325 |
| exposure | 0.2151 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
