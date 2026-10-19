# EMA Hourly Continuation — JST/USDT P21_55

**Symbol:** JST/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 816 |
| net_profit_factor | 0.3024 |
| net_win_rate | 0.4314 |
| gross_profit_factor | 1.0588 |
| gross_win_rate | 0.4963 |
| sharpe_ratio | -8.7275 |
| sortino_ratio | -3.5396 |
| max_drawdown | 0.9898 |
| cagr | -0.8357 |
| net_avg_win | 12.1886 |
| net_avg_loss | -30.5720 |
| avg_hold_time_bars | 6.0858 |
| exposure | 0.2247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
