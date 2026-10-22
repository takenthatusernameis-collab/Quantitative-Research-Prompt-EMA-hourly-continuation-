# EMA Hourly Continuation — FET/USDT P55_144

**Symbol:** FET/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.6878 |
| net_win_rate | 0.5064 |
| gross_profit_factor | 0.9996 |
| gross_win_rate | 0.5064 |
| sharpe_ratio | -2.4114 |
| sortino_ratio | -0.7331 |
| max_drawdown | 0.5989 |
| cagr | -0.2938 |
| net_avg_win | 54.3804 |
| net_avg_loss | -81.1300 |
| avg_hold_time_bars | 12.2554 |
| exposure | 0.2596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
