# EMA Hourly Continuation — WAVES/USDT P8_200

**Symbol:** WAVES/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.5076 |
| net_win_rate | 0.4479 |
| gross_profit_factor | 0.8674 |
| gross_win_rate | 0.4735 |
| sharpe_ratio | -4.9309 |
| sortino_ratio | -1.6640 |
| max_drawdown | 0.8768 |
| cagr | -0.5610 |
| net_avg_win | 34.3698 |
| net_avg_loss | -54.9224 |
| avg_hold_time_bars | 27.8034 |
| exposure | 0.7393 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
