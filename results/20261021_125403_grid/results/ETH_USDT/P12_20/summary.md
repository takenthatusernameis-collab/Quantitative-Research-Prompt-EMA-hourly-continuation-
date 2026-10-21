# EMA Hourly Continuation — ETH/USDT P12_20

**Symbol:** ETH/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 222 |
| net_profit_factor | 0.6924 |
| net_win_rate | 0.5225 |
| gross_profit_factor | 1.1057 |
| gross_win_rate | 0.5225 |
| sharpe_ratio | -1.7392 |
| sortino_ratio | -0.3746 |
| max_drawdown | 0.4103 |
| cagr | -0.1566 |
| net_avg_win | 67.5352 |
| net_avg_loss | -106.7420 |
| avg_hold_time_bars | 5.3468 |
| exposure | 0.0540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
