# EMA Hourly Continuation — DAG/USDT P21_34

**Symbol:** DAG/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1147 |
| net_profit_factor | 0.3205 |
| net_win_rate | 0.3540 |
| gross_profit_factor | 0.6451 |
| gross_win_rate | 0.3714 |
| sharpe_ratio | -13.1078 |
| sortino_ratio | -6.2918 |
| max_drawdown | 0.9998 |
| cagr | -0.9661 |
| net_avg_win | 11.6152 |
| net_avg_loss | -19.8566 |
| avg_hold_time_bars | 2.3226 |
| exposure | 0.1211 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
