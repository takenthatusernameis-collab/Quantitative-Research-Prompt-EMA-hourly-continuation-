# EMA Hourly Continuation — ADA/USDT P55_144

**Symbol:** ADA/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.8595 |
| net_win_rate | 0.5309 |
| gross_profit_factor | 1.1086 |
| gross_win_rate | 0.5309 |
| sharpe_ratio | -0.7347 |
| sortino_ratio | -0.1856 |
| max_drawdown | 0.2641 |
| cagr | -0.0838 |
| net_avg_win | 74.0155 |
| net_avg_loss | -97.4804 |
| avg_hold_time_bars | 16.4528 |
| exposure | 0.2296 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
