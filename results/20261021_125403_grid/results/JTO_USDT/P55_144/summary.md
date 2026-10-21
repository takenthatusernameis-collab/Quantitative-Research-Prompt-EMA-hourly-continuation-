# EMA Hourly Continuation — JTO/USDT P55_144

**Symbol:** JTO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.6407 |
| net_win_rate | 0.4331 |
| gross_profit_factor | 0.7744 |
| gross_win_rate | 0.4331 |
| sharpe_ratio | -2.6273 |
| sortino_ratio | -0.6886 |
| max_drawdown | 0.5671 |
| cagr | -0.2714 |
| net_avg_win | 65.6256 |
| net_avg_loss | -78.2711 |
| avg_hold_time_bars | 15.1715 |
| exposure | 0.2372 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
