# EMA Hourly Continuation — CARV/USDT P8_200

**Symbol:** CARV/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.8305 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 0.9962 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -1.1601 |
| sortino_ratio | -0.3307 |
| max_drawdown | 0.3313 |
| cagr | -0.1428 |
| net_avg_win | 82.2386 |
| net_avg_loss | -98.4040 |
| avg_hold_time_bars | 39.2835 |
| exposure | 0.7096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
