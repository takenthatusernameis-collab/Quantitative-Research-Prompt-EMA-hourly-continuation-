# EMA Hourly Continuation — ID/USDT P8_50

**Symbol:** ID/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 731 |
| net_profit_factor | 0.8065 |
| net_win_rate | 0.5048 |
| gross_profit_factor | 1.0541 |
| gross_win_rate | 0.5048 |
| sharpe_ratio | -2.1269 |
| sortino_ratio | -0.8227 |
| max_drawdown | 0.6678 |
| cagr | -0.3155 |
| net_avg_win | 69.5368 |
| net_avg_loss | -87.8897 |
| avg_hold_time_bars | 13.5663 |
| exposure | 0.4488 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
