# EMA Hourly Continuation — APT/USDT P50_144

**Symbol:** APT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.8617 |
| net_win_rate | 0.5234 |
| gross_profit_factor | 1.0756 |
| gross_win_rate | 0.5234 |
| sharpe_ratio | -0.7326 |
| sortino_ratio | -0.1952 |
| max_drawdown | 0.2793 |
| cagr | -0.0881 |
| net_avg_win | 71.9751 |
| net_avg_loss | -91.7269 |
| avg_hold_time_bars | 16.7164 |
| exposure | 0.2599 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
