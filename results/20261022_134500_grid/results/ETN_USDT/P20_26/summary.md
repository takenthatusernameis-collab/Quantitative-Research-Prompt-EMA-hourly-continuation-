# EMA Hourly Continuation — ETN/USDT P20_26

**Symbol:** ETN/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1080 |
| net_profit_factor | 0.1568 |
| net_win_rate | 0.2565 |
| gross_profit_factor | 0.3205 |
| gross_win_rate | 0.3009 |
| sharpe_ratio | -18.1269 |
| sortino_ratio | -9.5616 |
| max_drawdown | 1.0000 |
| cagr | -0.9945 |
| net_avg_win | 6.7137 |
| net_avg_loss | -14.7690 |
| avg_hold_time_bars | 2.2917 |
| exposure | 0.1344 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
