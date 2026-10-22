# EMA Hourly Continuation — WOO/USDT P20_21

**Symbol:** WOO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 195 |
| net_profit_factor | 0.6054 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.8666 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -2.2545 |
| sortino_ratio | -0.4502 |
| max_drawdown | 0.4506 |
| cagr | -0.1873 |
| net_avg_win | 69.1918 |
| net_avg_loss | -97.9663 |
| avg_hold_time_bars | 4.2872 |
| exposure | 0.0380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
