# EMA Hourly Continuation — REZ/USDT P100_144

**Symbol:** REZ/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.6756 |
| net_win_rate | 0.4699 |
| gross_profit_factor | 0.8709 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -1.9525 |
| sortino_ratio | -0.4572 |
| max_drawdown | 0.4190 |
| cagr | -0.1895 |
| net_avg_win | 67.5246 |
| net_avg_loss | -88.6093 |
| avg_hold_time_bars | 6.6316 |
| exposure | 0.0814 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
