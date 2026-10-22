# EMA Hourly Continuation — ZRO/USDT P20_26

**Symbol:** ZRO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1188 |
| net_profit_factor | 0.3259 |
| net_win_rate | 0.3771 |
| gross_profit_factor | 0.7257 |
| gross_win_rate | 0.4040 |
| sharpe_ratio | -13.2165 |
| sortino_ratio | -6.7626 |
| max_drawdown | 0.9997 |
| cagr | -0.9704 |
| net_avg_win | 10.7862 |
| net_avg_loss | -20.0399 |
| avg_hold_time_bars | 1.8923 |
| exposure | 0.1100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
