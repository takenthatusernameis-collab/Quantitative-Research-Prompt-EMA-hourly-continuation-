# EMA Hourly Continuation — SUI/USDT P8_12

**Symbol:** SUI/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 171 |
| net_profit_factor | 0.8907 |
| net_win_rate | 0.5497 |
| gross_profit_factor | 1.2115 |
| gross_win_rate | 0.5497 |
| sharpe_ratio | -0.4404 |
| sortino_ratio | -0.0837 |
| max_drawdown | 0.1381 |
| cagr | -0.0388 |
| net_avg_win | 81.9796 |
| net_avg_loss | -112.3551 |
| avg_hold_time_bars | 5.0409 |
| exposure | 0.0392 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
