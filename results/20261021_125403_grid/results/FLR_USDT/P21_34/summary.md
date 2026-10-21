# EMA Hourly Continuation — FLR/USDT P21_34

**Symbol:** FLR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.4971 |
| net_win_rate | 0.4110 |
| gross_profit_factor | 0.7325 |
| gross_win_rate | 0.4110 |
| sharpe_ratio | -4.2529 |
| sortino_ratio | -1.0986 |
| max_drawdown | 0.7328 |
| cagr | -0.3981 |
| net_avg_win | 53.1521 |
| net_avg_loss | -74.6220 |
| avg_hold_time_bars | 5.1626 |
| exposure | 0.0765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
