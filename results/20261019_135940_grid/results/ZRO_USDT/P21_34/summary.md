# EMA Hourly Continuation — ZRO/USDT P21_34

**Symbol:** ZRO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1114 |
| net_profit_factor | 0.4717 |
| net_win_rate | 0.4399 |
| gross_profit_factor | 0.8979 |
| gross_win_rate | 0.4551 |
| sharpe_ratio | -9.0269 |
| sortino_ratio | -4.4170 |
| max_drawdown | 0.9940 |
| cagr | -0.8879 |
| net_avg_win | 18.1130 |
| net_avg_loss | -30.1516 |
| avg_hold_time_bars | 2.4659 |
| exposure | 0.1345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
