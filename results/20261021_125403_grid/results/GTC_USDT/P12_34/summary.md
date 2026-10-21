# EMA Hourly Continuation — GTC/USDT P12_34

**Symbol:** GTC/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 651 |
| net_profit_factor | 0.6355 |
| net_win_rate | 0.4654 |
| gross_profit_factor | 0.8581 |
| gross_win_rate | 0.4654 |
| sharpe_ratio | -3.5962 |
| sortino_ratio | -1.3083 |
| max_drawdown | 0.7874 |
| cagr | -0.4518 |
| net_avg_win | 44.8302 |
| net_avg_loss | -61.4188 |
| avg_hold_time_bars | 6.8817 |
| exposure | 0.2036 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
