# EMA Hourly Continuation — DBR/USDT P21_26

**Symbol:** DBR/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 215 |
| net_profit_factor | 0.6209 |
| net_win_rate | 0.5256 |
| gross_profit_factor | 1.1658 |
| gross_win_rate | 0.5349 |
| sharpe_ratio | -2.3678 |
| sortino_ratio | -0.5564 |
| max_drawdown | 0.4655 |
| cagr | -0.2267 |
| net_avg_win | 58.4319 |
| net_avg_loss | -104.2556 |
| avg_hold_time_bars | 7.0791 |
| exposure | 0.0866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
