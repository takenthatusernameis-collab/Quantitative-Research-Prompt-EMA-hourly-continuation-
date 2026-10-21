# EMA Hourly Continuation — WIF/USDT P55_144

**Symbol:** WIF/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.8539 |
| net_win_rate | 0.5083 |
| gross_profit_factor | 1.0157 |
| gross_win_rate | 0.5083 |
| sharpe_ratio | -0.7764 |
| sortino_ratio | -0.1932 |
| max_drawdown | 0.2382 |
| cagr | -0.0873 |
| net_avg_win | 78.3397 |
| net_avg_loss | -94.8377 |
| avg_hold_time_bars | 16.0332 |
| exposure | 0.2194 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
