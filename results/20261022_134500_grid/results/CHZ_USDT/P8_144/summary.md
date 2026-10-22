# EMA Hourly Continuation — CHZ/USDT P8_144

**Symbol:** CHZ/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.6139 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 0.8972 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -3.1405 |
| sortino_ratio | -0.9852 |
| max_drawdown | 0.7083 |
| cagr | -0.3786 |
| net_avg_win | 46.5895 |
| net_avg_loss | -69.1991 |
| avg_hold_time_bars | 32.8577 |
| exposure | 0.7453 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
