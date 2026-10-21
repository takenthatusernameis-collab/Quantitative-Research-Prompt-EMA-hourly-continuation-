# EMA Hourly Continuation — ENA/USDT P26_34

**Symbol:** ENA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 172 |
| net_profit_factor | 0.7713 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9772 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.9782 |
| sortino_ratio | -0.1839 |
| max_drawdown | 0.2239 |
| cagr | -0.0814 |
| net_avg_win | 75.2772 |
| net_avg_loss | -97.5964 |
| avg_hold_time_bars | 4.6686 |
| exposure | 0.0365 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
