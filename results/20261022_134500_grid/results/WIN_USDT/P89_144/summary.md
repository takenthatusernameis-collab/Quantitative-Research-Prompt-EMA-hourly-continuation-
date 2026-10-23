# EMA Hourly Continuation — WIN/USDT P89_144

**Symbol:** WIN/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.2627 |
| net_win_rate | 0.3848 |
| gross_profit_factor | 0.6271 |
| gross_win_rate | 0.4115 |
| sharpe_ratio | -7.6197 |
| sortino_ratio | -2.4022 |
| max_drawdown | 0.9554 |
| cagr | -0.7102 |
| net_avg_win | 18.2071 |
| net_avg_loss | -43.3413 |
| avg_hold_time_bars | 5.1111 |
| exposure | 0.1129 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
