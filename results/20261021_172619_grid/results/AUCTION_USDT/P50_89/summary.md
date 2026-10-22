# EMA Hourly Continuation — AUCTION/USDT P50_89

**Symbol:** AUCTION/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.5750 |
| net_win_rate | 0.4531 |
| gross_profit_factor | 0.8583 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -4.0302 |
| sortino_ratio | -1.1843 |
| max_drawdown | 0.7736 |
| cagr | -0.4338 |
| net_avg_win | 52.0563 |
| net_avg_loss | -74.9996 |
| avg_hold_time_bars | 7.5492 |
| exposure | 0.1493 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
