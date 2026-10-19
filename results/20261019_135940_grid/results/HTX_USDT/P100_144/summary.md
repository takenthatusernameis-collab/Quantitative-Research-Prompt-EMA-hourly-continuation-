# EMA Hourly Continuation — HTX/USDT P100_144

**Symbol:** HTX/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 558 |
| net_profit_factor | 0.1430 |
| net_win_rate | 0.2401 |
| gross_profit_factor | 0.4920 |
| gross_win_rate | 0.3082 |
| sharpe_ratio | -12.9437 |
| sortino_ratio | -4.7538 |
| max_drawdown | 0.9985 |
| cagr | -0.9232 |
| net_avg_win | 12.4341 |
| net_avg_loss | -27.4781 |
| avg_hold_time_bars | 4.4588 |
| exposure | 0.1126 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
