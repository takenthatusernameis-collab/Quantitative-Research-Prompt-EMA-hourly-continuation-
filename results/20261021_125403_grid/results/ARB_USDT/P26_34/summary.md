# EMA Hourly Continuation — ARB/USDT P26_34

**Symbol:** ARB/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 156 |
| net_profit_factor | 0.7721 |
| net_win_rate | 0.5192 |
| gross_profit_factor | 1.0703 |
| gross_win_rate | 0.5192 |
| sharpe_ratio | -0.9710 |
| sortino_ratio | -0.1749 |
| max_drawdown | 0.2035 |
| cagr | -0.0769 |
| net_avg_win | 76.1817 |
| net_avg_loss | -106.5594 |
| avg_hold_time_bars | 5.6346 |
| exposure | 0.0400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
