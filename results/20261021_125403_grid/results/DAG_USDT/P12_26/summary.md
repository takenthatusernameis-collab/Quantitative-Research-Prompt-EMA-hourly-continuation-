# EMA Hourly Continuation — DAG/USDT P12_26

**Symbol:** DAG/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.6666 |
| net_win_rate | 0.4681 |
| gross_profit_factor | 0.8487 |
| gross_win_rate | 0.4681 |
| sharpe_ratio | -1.9886 |
| sortino_ratio | -0.4753 |
| max_drawdown | 0.4360 |
| cagr | -0.1960 |
| net_avg_win | 63.8802 |
| net_avg_loss | -84.3366 |
| avg_hold_time_bars | 6.1986 |
| exposure | 0.0795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
