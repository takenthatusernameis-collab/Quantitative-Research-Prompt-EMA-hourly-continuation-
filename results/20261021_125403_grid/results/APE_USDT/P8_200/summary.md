# EMA Hourly Continuation — APE/USDT P8_200

**Symbol:** APE/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 206 |
| net_profit_factor | 0.7132 |
| net_win_rate | 0.4612 |
| gross_profit_factor | 0.8435 |
| gross_win_rate | 0.4612 |
| sharpe_ratio | -1.4289 |
| sortino_ratio | -0.2912 |
| max_drawdown | 0.2860 |
| cagr | -0.1255 |
| net_avg_win | 74.8650 |
| net_avg_loss | -89.8406 |
| avg_hold_time_bars | 90.7524 |
| exposure | 0.8498 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
