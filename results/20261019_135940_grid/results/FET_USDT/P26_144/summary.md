# EMA Hourly Continuation — FET/USDT P26_144

**Symbol:** FET/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.7456 |
| net_win_rate | 0.5056 |
| gross_profit_factor | 1.0039 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -1.8299 |
| sortino_ratio | -0.5427 |
| max_drawdown | 0.5155 |
| cagr | -0.2288 |
| net_avg_win | 62.6987 |
| net_avg_loss | -86.0161 |
| avg_hold_time_bars | 24.3409 |
| exposure | 0.4901 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
