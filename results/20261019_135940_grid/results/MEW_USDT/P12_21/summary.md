# EMA Hourly Continuation — MEW/USDT P12_21

**Symbol:** MEW/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1463 |
| net_profit_factor | 0.4750 |
| net_win_rate | 0.4149 |
| gross_profit_factor | 0.8913 |
| gross_win_rate | 0.4436 |
| sharpe_ratio | -11.5187 |
| sortino_ratio | -6.2192 |
| max_drawdown | 0.9996 |
| cagr | -0.9571 |
| net_avg_win | 14.8993 |
| net_avg_loss | -22.2432 |
| avg_hold_time_bars | 2.3233 |
| exposure | 0.1545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
