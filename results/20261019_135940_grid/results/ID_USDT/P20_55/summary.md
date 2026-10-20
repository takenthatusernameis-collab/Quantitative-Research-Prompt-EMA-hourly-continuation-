# EMA Hourly Continuation — ID/USDT P20_55

**Symbol:** ID/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 874 |
| net_profit_factor | 0.5216 |
| net_win_rate | 0.4645 |
| gross_profit_factor | 0.9223 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -5.7903 |
| sortino_ratio | -2.4099 |
| max_drawdown | 0.9470 |
| cagr | -0.6854 |
| net_avg_win | 25.4052 |
| net_avg_loss | -42.2513 |
| avg_hold_time_bars | 6.4371 |
| exposure | 0.2546 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
