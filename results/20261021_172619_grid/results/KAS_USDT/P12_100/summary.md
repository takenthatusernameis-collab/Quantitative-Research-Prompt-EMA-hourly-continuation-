# EMA Hourly Continuation — KAS/USDT P12_100

**Symbol:** KAS/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.8528 |
| net_win_rate | 0.5177 |
| gross_profit_factor | 1.0484 |
| gross_win_rate | 0.5177 |
| sharpe_ratio | -0.9703 |
| sortino_ratio | -0.3057 |
| max_drawdown | 0.3302 |
| cagr | -0.1340 |
| net_avg_win | 70.5483 |
| net_avg_loss | -88.7893 |
| avg_hold_time_bars | 24.4657 |
| exposure | 0.5349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
