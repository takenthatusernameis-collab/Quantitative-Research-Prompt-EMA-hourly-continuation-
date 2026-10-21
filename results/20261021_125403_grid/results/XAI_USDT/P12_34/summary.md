# EMA Hourly Continuation — XAI/USDT P12_34

**Symbol:** XAI/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.7190 |
| net_win_rate | 0.4700 |
| gross_profit_factor | 0.9178 |
| gross_win_rate | 0.4700 |
| sharpe_ratio | -3.1586 |
| sortino_ratio | -1.1617 |
| max_drawdown | 0.7497 |
| cagr | -0.4133 |
| net_avg_win | 60.3261 |
| net_avg_loss | -74.3940 |
| avg_hold_time_bars | 7.0676 |
| exposure | 0.2140 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
