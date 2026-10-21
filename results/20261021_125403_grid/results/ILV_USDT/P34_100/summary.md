# EMA Hourly Continuation — ILV/USDT P34_100

**Symbol:** ILV/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.8008 |
| net_win_rate | 0.5055 |
| gross_profit_factor | 1.0285 |
| gross_win_rate | 0.5055 |
| sharpe_ratio | -1.5766 |
| sortino_ratio | -0.4814 |
| max_drawdown | 0.4822 |
| cagr | -0.1991 |
| net_avg_win | 75.0344 |
| net_avg_loss | -95.7913 |
| avg_hold_time_bars | 13.5386 |
| exposure | 0.2788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
