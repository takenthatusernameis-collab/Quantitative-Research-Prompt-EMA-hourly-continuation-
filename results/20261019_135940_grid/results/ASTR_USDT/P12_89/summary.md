# EMA Hourly Continuation — ASTR/USDT P12_89

**Symbol:** ASTR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.6342 |
| net_win_rate | 0.4912 |
| gross_profit_factor | 0.9943 |
| gross_win_rate | 0.5059 |
| sharpe_ratio | -3.6317 |
| sortino_ratio | -1.3256 |
| max_drawdown | 0.8087 |
| cagr | -0.4726 |
| net_avg_win | 41.7005 |
| net_avg_loss | -63.4643 |
| avg_hold_time_bars | 18.1372 |
| exposure | 0.5565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
