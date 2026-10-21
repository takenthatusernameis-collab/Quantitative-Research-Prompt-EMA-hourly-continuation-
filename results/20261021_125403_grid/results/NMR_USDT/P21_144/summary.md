# EMA Hourly Continuation — NMR/USDT P21_144

**Symbol:** NMR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.7464 |
| net_win_rate | 0.4853 |
| gross_profit_factor | 0.9336 |
| gross_win_rate | 0.4853 |
| sharpe_ratio | -1.9815 |
| sortino_ratio | -0.5941 |
| max_drawdown | 0.5197 |
| cagr | -0.2393 |
| net_avg_win | 68.0229 |
| net_avg_loss | -85.9329 |
| avg_hold_time_bars | 25.2889 |
| exposure | 0.5092 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
