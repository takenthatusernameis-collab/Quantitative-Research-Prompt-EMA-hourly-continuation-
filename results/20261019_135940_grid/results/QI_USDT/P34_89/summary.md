# EMA Hourly Continuation — QI/USDT P34_89

**Symbol:** QI/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.5988 |
| net_win_rate | 0.4898 |
| gross_profit_factor | 1.0164 |
| gross_win_rate | 0.4992 |
| sharpe_ratio | -3.9950 |
| sortino_ratio | -1.4215 |
| max_drawdown | 0.8239 |
| cagr | -0.4918 |
| net_avg_win | 39.2884 |
| net_avg_loss | -62.9792 |
| avg_hold_time_bars | 7.9197 |
| exposure | 0.2276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
