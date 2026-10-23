# EMA Hourly Continuation — GMT/USDT P55_144

**Symbol:** GMT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.5888 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.9533 |
| gross_win_rate | 0.4765 |
| sharpe_ratio | -3.9241 |
| sortino_ratio | -1.2490 |
| max_drawdown | 0.7953 |
| cagr | -0.4509 |
| net_avg_win | 46.4236 |
| net_avg_loss | -70.0845 |
| avg_hold_time_bars | 10.6137 |
| exposure | 0.2460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
