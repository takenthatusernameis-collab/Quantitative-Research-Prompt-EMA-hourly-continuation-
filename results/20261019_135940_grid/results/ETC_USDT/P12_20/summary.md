# EMA Hourly Continuation — ETC/USDT P12_20

**Symbol:** ETC/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1493 |
| net_profit_factor | 0.2332 |
| net_win_rate | 0.3637 |
| gross_profit_factor | 0.9170 |
| gross_win_rate | 0.4313 |
| sharpe_ratio | -16.6834 |
| sortino_ratio | -9.4293 |
| max_drawdown | 1.0000 |
| cagr | -0.9938 |
| net_avg_win | 5.6011 |
| net_avg_loss | -13.7278 |
| avg_hold_time_bars | 2.1112 |
| exposure | 0.1433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
