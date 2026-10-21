# EMA Hourly Continuation — ONT/USDT P89_144

**Symbol:** ONT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.6467 |
| net_win_rate | 0.4849 |
| gross_profit_factor | 0.9007 |
| gross_win_rate | 0.4849 |
| sharpe_ratio | -2.1320 |
| sortino_ratio | -0.5262 |
| max_drawdown | 0.4692 |
| cagr | -0.2145 |
| net_avg_win | 57.5656 |
| net_avg_loss | -83.8155 |
| avg_hold_time_bars | 7.9599 |
| exposure | 0.1077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
