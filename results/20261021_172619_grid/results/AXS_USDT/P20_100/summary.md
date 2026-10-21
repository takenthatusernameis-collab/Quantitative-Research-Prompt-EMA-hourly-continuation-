# EMA Hourly Continuation — AXS/USDT P20_100

**Symbol:** AXS/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.8580 |
| net_win_rate | 0.5190 |
| gross_profit_factor | 1.0753 |
| gross_win_rate | 0.5190 |
| sharpe_ratio | -0.9715 |
| sortino_ratio | -0.2948 |
| max_drawdown | 0.3205 |
| cagr | -0.1293 |
| net_avg_win | 76.7553 |
| net_avg_loss | -96.5313 |
| avg_hold_time_bars | 20.7987 |
| exposure | 0.4207 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
