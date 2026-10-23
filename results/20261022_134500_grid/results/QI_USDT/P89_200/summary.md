# EMA Hourly Continuation — QI/USDT P89_200

**Symbol:** QI/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.5742 |
| net_win_rate | 0.4704 |
| gross_profit_factor | 0.8901 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -3.2177 |
| sortino_ratio | -0.9162 |
| max_drawdown | 0.6625 |
| cagr | -0.3487 |
| net_avg_win | 46.6597 |
| net_avg_loss | -72.1933 |
| avg_hold_time_bars | 11.1552 |
| exposure | 0.2049 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
