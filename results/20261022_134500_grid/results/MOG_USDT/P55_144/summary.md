# EMA Hourly Continuation — MOG/USDT P55_144

**Symbol:** MOG/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.6521 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.8559 |
| gross_win_rate | 0.4593 |
| sharpe_ratio | -3.2952 |
| sortino_ratio | -1.0397 |
| max_drawdown | 0.7147 |
| cagr | -0.3844 |
| net_avg_win | 60.5369 |
| net_avg_loss | -78.1766 |
| avg_hold_time_bars | 10.0242 |
| exposure | 0.2267 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
