# EMA Hourly Continuation — CPOOL/USDT P50_144

**Symbol:** CPOOL/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 588 |
| net_profit_factor | 0.5989 |
| net_win_rate | 0.4405 |
| gross_profit_factor | 0.8327 |
| gross_win_rate | 0.4456 |
| sharpe_ratio | -4.4568 |
| sortino_ratio | -1.5150 |
| max_drawdown | 0.8545 |
| cagr | -0.5172 |
| net_avg_win | 48.3841 |
| net_avg_loss | -63.6023 |
| avg_hold_time_bars | 8.6514 |
| exposure | 0.2312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
