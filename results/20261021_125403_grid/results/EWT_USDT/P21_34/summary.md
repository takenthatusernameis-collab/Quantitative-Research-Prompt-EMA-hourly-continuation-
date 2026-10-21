# EMA Hourly Continuation — EWT/USDT P21_34

**Symbol:** EWT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 246 |
| net_profit_factor | 0.5859 |
| net_win_rate | 0.4512 |
| gross_profit_factor | 0.8096 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -2.5652 |
| sortino_ratio | -0.5727 |
| max_drawdown | 0.4929 |
| cagr | -0.2321 |
| net_avg_win | 61.8027 |
| net_avg_loss | -86.7318 |
| avg_hold_time_bars | 7.0528 |
| exposure | 0.0789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
