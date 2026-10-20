# EMA Hourly Continuation — WIN/USDT P20_21

**Symbol:** WIN/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1183 |
| net_profit_factor | 0.0702 |
| net_win_rate | 0.2257 |
| gross_profit_factor | 0.5108 |
| gross_win_rate | 0.3238 |
| sharpe_ratio | -20.9190 |
| sortino_ratio | -11.9540 |
| max_drawdown | 1.0000 |
| cagr | -0.9988 |
| net_avg_win | 2.8284 |
| net_avg_loss | -11.7415 |
| avg_hold_time_bars | 1.6331 |
| exposure | 0.0878 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
