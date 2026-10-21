# EMA Hourly Continuation — ZIL/USDT P20_144

**Symbol:** ZIL/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.8750 |
| net_win_rate | 0.5229 |
| gross_profit_factor | 1.0962 |
| gross_win_rate | 0.5229 |
| sharpe_ratio | -0.8234 |
| sortino_ratio | -0.2280 |
| max_drawdown | 0.3735 |
| cagr | -0.1026 |
| net_avg_win | 85.8808 |
| net_avg_loss | -107.5746 |
| avg_hold_time_bars | 32.1051 |
| exposure | 0.5414 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
