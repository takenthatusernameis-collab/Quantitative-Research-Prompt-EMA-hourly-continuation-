# EMA Hourly Continuation — ZRO/USDT P12_21

**Symbol:** ZRO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.7952 |
| net_win_rate | 0.5041 |
| gross_profit_factor | 1.0235 |
| gross_win_rate | 0.5041 |
| sharpe_ratio | -1.2070 |
| sortino_ratio | -0.2808 |
| max_drawdown | 0.3788 |
| cagr | -0.1215 |
| net_avg_win | 82.2910 |
| net_avg_loss | -105.1952 |
| avg_hold_time_bars | 4.5287 |
| exposure | 0.0541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
