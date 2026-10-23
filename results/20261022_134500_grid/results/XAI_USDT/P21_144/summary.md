# EMA Hourly Continuation — XAI/USDT P21_144

**Symbol:** XAI/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.6850 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 0.9292 |
| gross_win_rate | 0.4664 |
| sharpe_ratio | -3.4317 |
| sortino_ratio | -1.0974 |
| max_drawdown | 0.7821 |
| cagr | -0.4082 |
| net_avg_win | 66.3315 |
| net_avg_loss | -82.7083 |
| avg_hold_time_bars | 24.3839 |
| exposure | 0.5775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
