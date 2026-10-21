# EMA Hourly Continuation — JUP/USDT P20_144

**Symbol:** JUP/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.8069 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 0.9434 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -1.3156 |
| sortino_ratio | -0.3615 |
| max_drawdown | 0.4024 |
| cagr | -0.1543 |
| net_avg_win | 79.3404 |
| net_avg_loss | -93.1763 |
| avg_hold_time_bars | 29.2231 |
| exposure | 0.4941 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
