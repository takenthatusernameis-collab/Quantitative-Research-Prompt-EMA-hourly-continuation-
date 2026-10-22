# EMA Hourly Continuation — ENA/USDT P55_144

**Symbol:** ENA/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.6891 |
| net_win_rate | 0.4767 |
| gross_profit_factor | 0.9148 |
| gross_win_rate | 0.4809 |
| sharpe_ratio | -2.5504 |
| sortino_ratio | -0.7877 |
| max_drawdown | 0.6204 |
| cagr | -0.3057 |
| net_avg_win | 59.1047 |
| net_avg_loss | -78.1305 |
| avg_hold_time_bars | 9.8538 |
| exposure | 0.2114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
