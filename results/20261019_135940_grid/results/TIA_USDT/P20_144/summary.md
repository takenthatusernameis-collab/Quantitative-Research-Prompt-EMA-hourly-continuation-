# EMA Hourly Continuation — TIA/USDT P20_144

**Symbol:** TIA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.7743 |
| net_win_rate | 0.4943 |
| gross_profit_factor | 1.0075 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -1.7997 |
| sortino_ratio | -0.5343 |
| max_drawdown | 0.4746 |
| cagr | -0.2210 |
| net_avg_win | 74.3688 |
| net_avg_loss | -93.8590 |
| avg_hold_time_bars | 28.8368 |
| exposure | 0.5702 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
