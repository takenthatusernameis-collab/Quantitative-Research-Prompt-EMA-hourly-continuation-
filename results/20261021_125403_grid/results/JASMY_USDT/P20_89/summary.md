# EMA Hourly Continuation — JASMY/USDT P20_89

**Symbol:** JASMY/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.8794 |
| net_win_rate | 0.5242 |
| gross_profit_factor | 1.0849 |
| gross_win_rate | 0.5242 |
| sharpe_ratio | -0.8214 |
| sortino_ratio | -0.2635 |
| max_drawdown | 0.3423 |
| cagr | -0.1179 |
| net_avg_win | 75.7951 |
| net_avg_loss | -94.9566 |
| avg_hold_time_bars | 14.9698 |
| exposure | 0.3375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
