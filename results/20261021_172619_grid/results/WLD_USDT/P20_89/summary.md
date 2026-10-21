# EMA Hourly Continuation — WLD/USDT P20_89

**Symbol:** WLD/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 1.0390 |
| net_win_rate | 0.5533 |
| gross_profit_factor | 1.2253 |
| gross_win_rate | 0.5533 |
| sharpe_ratio | 0.3236 |
| sortino_ratio | 0.0999 |
| max_drawdown | 0.2047 |
| cagr | 0.0349 |
| net_avg_win | 96.3335 |
| net_avg_loss | -114.8636 |
| avg_hold_time_bars | 17.8400 |
| exposure | 0.3649 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
