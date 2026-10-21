# EMA Hourly Continuation — TRB/USDT P34_50

**Symbol:** TRB/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.6306 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.8937 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -2.6853 |
| sortino_ratio | -0.6446 |
| max_drawdown | 0.5622 |
| cagr | -0.2565 |
| net_avg_win | 68.6073 |
| net_avg_loss | -93.7718 |
| avg_hold_time_bars | 4.4170 |
| exposure | 0.0566 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
