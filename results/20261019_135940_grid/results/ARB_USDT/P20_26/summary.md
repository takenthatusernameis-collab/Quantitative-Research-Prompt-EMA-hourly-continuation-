# EMA Hourly Continuation — ARB/USDT P20_26

**Symbol:** ARB/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1177 |
| net_profit_factor | 0.1962 |
| net_win_rate | 0.3857 |
| gross_profit_factor | 0.7184 |
| gross_win_rate | 0.4231 |
| sharpe_ratio | -13.3137 |
| sortino_ratio | -6.5959 |
| max_drawdown | 0.9998 |
| cagr | -0.9697 |
| net_avg_win | 5.3763 |
| net_avg_loss | -17.2051 |
| avg_hold_time_bars | 1.9040 |
| exposure | 0.1019 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
