# EMA Hourly Continuation — RSR/USDT P21_200

**Symbol:** RSR/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.9160 |
| net_win_rate | 0.5154 |
| gross_profit_factor | 1.0575 |
| gross_win_rate | 0.5154 |
| sharpe_ratio | -0.4617 |
| sortino_ratio | -0.1194 |
| max_drawdown | 0.1933 |
| cagr | -0.0573 |
| net_avg_win | 89.9793 |
| net_avg_loss | -104.4851 |
| avg_hold_time_bars | 40.9074 |
| exposure | 0.6025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
