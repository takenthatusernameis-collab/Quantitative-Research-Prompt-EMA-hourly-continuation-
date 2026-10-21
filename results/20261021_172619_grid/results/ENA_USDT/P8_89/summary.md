# EMA Hourly Continuation — ENA/USDT P8_89

**Symbol:** ENA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.9139 |
| net_win_rate | 0.5134 |
| gross_profit_factor | 1.0477 |
| gross_win_rate | 0.5134 |
| sharpe_ratio | -0.5933 |
| sortino_ratio | -0.1951 |
| max_drawdown | 0.3733 |
| cagr | -0.0916 |
| net_avg_win | 84.5825 |
| net_avg_loss | -97.6297 |
| avg_hold_time_bars | 24.5534 |
| exposure | 0.5848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
