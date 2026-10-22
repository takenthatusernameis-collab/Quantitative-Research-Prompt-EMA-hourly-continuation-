# EMA Hourly Continuation — REZ/USDT P12_26

**Symbol:** REZ/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 558 |
| net_profit_factor | 0.7185 |
| net_win_rate | 0.4785 |
| gross_profit_factor | 0.9370 |
| gross_win_rate | 0.4785 |
| sharpe_ratio | -2.7484 |
| sortino_ratio | -0.9342 |
| max_drawdown | 0.6744 |
| cagr | -0.3489 |
| net_avg_win | 62.5359 |
| net_avg_loss | -79.8565 |
| avg_hold_time_bars | 5.7832 |
| exposure | 0.1489 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
