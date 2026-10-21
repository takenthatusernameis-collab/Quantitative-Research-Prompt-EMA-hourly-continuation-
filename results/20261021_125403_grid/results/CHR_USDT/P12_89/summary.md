# EMA Hourly Continuation — CHR/USDT P12_89

**Symbol:** CHR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.7653 |
| net_win_rate | 0.4767 |
| gross_profit_factor | 0.9218 |
| gross_win_rate | 0.4767 |
| sharpe_ratio | -2.0257 |
| sortino_ratio | -0.6526 |
| max_drawdown | 0.5523 |
| cagr | -0.2607 |
| net_avg_win | 70.9920 |
| net_avg_loss | -84.4841 |
| avg_hold_time_bars | 24.2588 |
| exposure | 0.5642 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
