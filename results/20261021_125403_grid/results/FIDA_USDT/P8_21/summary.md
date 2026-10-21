# EMA Hourly Continuation — FIDA/USDT P8_21

**Symbol:** FIDA/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 726 |
| net_profit_factor | 0.6328 |
| net_win_rate | 0.4835 |
| gross_profit_factor | 0.8891 |
| gross_win_rate | 0.4835 |
| sharpe_ratio | -3.5374 |
| sortino_ratio | -1.3597 |
| max_drawdown | 0.7941 |
| cagr | -0.4655 |
| net_avg_win | 38.9852 |
| net_avg_loss | -57.6656 |
| avg_hold_time_bars | 6.2121 |
| exposure | 0.2041 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
