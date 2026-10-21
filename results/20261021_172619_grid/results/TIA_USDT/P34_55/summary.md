# EMA Hourly Continuation — TIA/USDT P34_55

**Symbol:** TIA/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.8185 |
| net_win_rate | 0.5115 |
| gross_profit_factor | 1.0527 |
| gross_win_rate | 0.5115 |
| sharpe_ratio | -1.1401 |
| sortino_ratio | -0.2863 |
| max_drawdown | 0.3362 |
| cagr | -0.1238 |
| net_avg_win | 81.6742 |
| net_avg_loss | -104.4706 |
| avg_hold_time_bars | 5.9344 |
| exposure | 0.0823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
