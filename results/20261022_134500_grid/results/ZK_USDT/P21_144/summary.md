# EMA Hourly Continuation — ZK/USDT P21_144

**Symbol:** ZK/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.6815 |
| net_win_rate | 0.4647 |
| gross_profit_factor | 0.9107 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -3.0847 |
| sortino_ratio | -1.0170 |
| max_drawdown | 0.6834 |
| cagr | -0.3808 |
| net_avg_win | 60.8783 |
| net_avg_loss | -77.5547 |
| avg_hold_time_bars | 20.8824 |
| exposure | 0.5192 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
