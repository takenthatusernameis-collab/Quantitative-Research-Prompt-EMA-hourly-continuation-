# EMA Hourly Continuation — DAG/USDT P12_55

**Symbol:** DAG/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.8378 |
| net_win_rate | 0.5060 |
| gross_profit_factor | 1.0092 |
| gross_win_rate | 0.5060 |
| sharpe_ratio | -1.2109 |
| sortino_ratio | -0.3889 |
| max_drawdown | 0.4379 |
| cagr | -0.1661 |
| net_avg_win | 74.4968 |
| net_avg_loss | -91.0686 |
| avg_hold_time_bars | 12.5438 |
| exposure | 0.2862 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
