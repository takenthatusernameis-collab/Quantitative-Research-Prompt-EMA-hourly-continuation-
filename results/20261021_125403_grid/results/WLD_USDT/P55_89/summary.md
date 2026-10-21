# EMA Hourly Continuation — WLD/USDT P55_89

**Symbol:** WLD/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 259 |
| net_profit_factor | 0.9377 |
| net_win_rate | 0.5444 |
| gross_profit_factor | 1.1810 |
| gross_win_rate | 0.5444 |
| sharpe_ratio | -0.2607 |
| sortino_ratio | -0.0609 |
| max_drawdown | 0.1746 |
| cagr | -0.0311 |
| net_avg_win | 81.3384 |
| net_avg_loss | -103.6485 |
| avg_hold_time_bars | 7.5367 |
| exposure | 0.0887 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
