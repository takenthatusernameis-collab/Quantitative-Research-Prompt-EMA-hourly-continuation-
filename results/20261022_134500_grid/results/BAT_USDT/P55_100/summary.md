# EMA Hourly Continuation — BAT/USDT P55_100

**Symbol:** BAT/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 600 |
| net_profit_factor | 0.4454 |
| net_win_rate | 0.4450 |
| gross_profit_factor | 0.8736 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -5.5888 |
| sortino_ratio | -1.9351 |
| max_drawdown | 0.9048 |
| cagr | -0.6060 |
| net_avg_win | 27.1737 |
| net_avg_loss | -48.9227 |
| avg_hold_time_bars | 5.1100 |
| exposure | 0.1394 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
