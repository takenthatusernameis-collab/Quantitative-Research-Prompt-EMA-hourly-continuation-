# EMA Hourly Continuation — CETUS/USDT P144_200

**Symbol:** CETUS/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.5273 |
| net_win_rate | 0.4338 |
| gross_profit_factor | 0.8255 |
| gross_win_rate | 0.4479 |
| sharpe_ratio | -4.0650 |
| sortino_ratio | -1.0777 |
| max_drawdown | 0.7319 |
| cagr | -0.4043 |
| net_avg_win | 52.8199 |
| net_avg_loss | -76.7526 |
| avg_hold_time_bars | 4.7268 |
| exposure | 0.0759 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
