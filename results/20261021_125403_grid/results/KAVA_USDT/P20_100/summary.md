# EMA Hourly Continuation — KAVA/USDT P20_100

**Symbol:** KAVA/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.7126 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 0.9648 |
| gross_win_rate | 0.4844 |
| sharpe_ratio | -2.6190 |
| sortino_ratio | -0.8195 |
| max_drawdown | 0.6411 |
| cagr | -0.3150 |
| net_avg_win | 65.2617 |
| net_avg_loss | -86.0462 |
| avg_hold_time_bars | 21.2287 |
| exposure | 0.4641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
