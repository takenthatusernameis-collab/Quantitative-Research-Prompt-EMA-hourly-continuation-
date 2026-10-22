# EMA Hourly Continuation — UMA/USDT P20_21

**Symbol:** UMA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 262 |
| net_profit_factor | 0.5493 |
| net_win_rate | 0.4733 |
| gross_profit_factor | 0.9190 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -3.0468 |
| sortino_ratio | -0.7027 |
| max_drawdown | 0.5865 |
| cagr | -0.2805 |
| net_avg_win | 55.2904 |
| net_avg_loss | -90.4442 |
| avg_hold_time_bars | 5.5954 |
| exposure | 0.0666 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
