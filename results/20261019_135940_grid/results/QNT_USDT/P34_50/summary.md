# EMA Hourly Continuation — QNT/USDT P34_50

**Symbol:** QNT/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1013 |
| net_profit_factor | 0.2419 |
| net_win_rate | 0.3909 |
| gross_profit_factor | 0.7052 |
| gross_win_rate | 0.4284 |
| sharpe_ratio | -11.8780 |
| sortino_ratio | -5.4523 |
| max_drawdown | 0.9991 |
| cagr | -0.9387 |
| net_avg_win | 8.0487 |
| net_avg_loss | -21.3586 |
| avg_hold_time_bars | 2.5133 |
| exposure | 0.1157 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
