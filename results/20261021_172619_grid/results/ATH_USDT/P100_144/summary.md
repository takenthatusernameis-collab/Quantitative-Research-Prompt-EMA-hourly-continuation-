# EMA Hourly Continuation — ATH/USDT P100_144

**Symbol:** ATH/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 232 |
| net_profit_factor | 0.6634 |
| net_win_rate | 0.4655 |
| gross_profit_factor | 0.8682 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -2.0059 |
| sortino_ratio | -0.4499 |
| max_drawdown | 0.4037 |
| cagr | -0.1867 |
| net_avg_win | 70.3100 |
| net_avg_loss | -92.3065 |
| avg_hold_time_bars | 6.9698 |
| exposure | 0.0784 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
