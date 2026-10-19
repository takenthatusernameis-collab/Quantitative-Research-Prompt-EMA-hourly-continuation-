# EMA Hourly Continuation — CVX/USDT P12_55

**Symbol:** CVX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1012 |
| net_profit_factor | 0.5505 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.8278 |
| gross_win_rate | 0.4674 |
| sharpe_ratio | -5.7731 |
| sortino_ratio | -2.5671 |
| max_drawdown | 0.9580 |
| cagr | -0.7152 |
| net_avg_win | 25.1017 |
| net_avg_loss | -39.0747 |
| avg_hold_time_bars | 8.0860 |
| exposure | 0.3720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
