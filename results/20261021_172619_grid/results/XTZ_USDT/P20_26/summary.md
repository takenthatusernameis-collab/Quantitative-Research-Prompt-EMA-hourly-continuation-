# EMA Hourly Continuation — XTZ/USDT P20_26

**Symbol:** XTZ/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.5664 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 0.9237 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -2.8041 |
| sortino_ratio | -0.6460 |
| max_drawdown | 0.5401 |
| cagr | -0.2551 |
| net_avg_win | 55.9536 |
| net_avg_loss | -90.6202 |
| avg_hold_time_bars | 4.4627 |
| exposure | 0.0517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
