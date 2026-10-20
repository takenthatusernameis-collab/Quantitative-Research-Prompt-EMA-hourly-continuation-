# EMA Hourly Continuation — CETUS/USDT P20_34

**Symbol:** CETUS/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1147 |
| net_profit_factor | 0.4874 |
| net_win_rate | 0.4185 |
| gross_profit_factor | 0.9798 |
| gross_win_rate | 0.4429 |
| sharpe_ratio | -9.8213 |
| sortino_ratio | -4.6844 |
| max_drawdown | 0.9974 |
| cagr | -0.9058 |
| net_avg_win | 19.7542 |
| net_avg_loss | -29.1697 |
| avg_hold_time_bars | 2.8326 |
| exposure | 0.1470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
