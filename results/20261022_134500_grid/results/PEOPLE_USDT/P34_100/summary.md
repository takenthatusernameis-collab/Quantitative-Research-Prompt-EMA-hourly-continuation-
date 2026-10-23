# EMA Hourly Continuation — PEOPLE/USDT P34_100

**Symbol:** PEOPLE/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.6487 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 0.9253 |
| gross_win_rate | 0.4835 |
| sharpe_ratio | -3.3926 |
| sortino_ratio | -1.2098 |
| max_drawdown | 0.7754 |
| cagr | -0.4332 |
| net_avg_win | 46.0892 |
| net_avg_loss | -65.6664 |
| avg_hold_time_bars | 9.7953 |
| exposure | 0.2815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
