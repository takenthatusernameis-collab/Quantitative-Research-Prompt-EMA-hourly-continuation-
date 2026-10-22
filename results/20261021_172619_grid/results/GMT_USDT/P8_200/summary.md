# EMA Hourly Continuation — GMT/USDT P8_200

**Symbol:** GMT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 246 |
| net_profit_factor | 0.9866 |
| net_win_rate | 0.5407 |
| gross_profit_factor | 1.1567 |
| gross_win_rate | 0.5407 |
| sharpe_ratio | -0.0120 |
| sortino_ratio | -0.0027 |
| max_drawdown | 0.2134 |
| cagr | -0.0061 |
| net_avg_win | 83.5258 |
| net_avg_loss | -99.6482 |
| avg_hold_time_bars | 74.1423 |
| exposure | 0.8290 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
