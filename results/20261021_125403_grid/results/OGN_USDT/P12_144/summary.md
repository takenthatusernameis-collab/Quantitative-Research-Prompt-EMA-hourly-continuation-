# EMA Hourly Continuation — OGN/USDT P12_144

**Symbol:** OGN/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.6535 |
| net_win_rate | 0.4508 |
| gross_profit_factor | 0.8229 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -2.6176 |
| sortino_ratio | -0.7060 |
| max_drawdown | 0.5893 |
| cagr | -0.2802 |
| net_avg_win | 64.4293 |
| net_avg_loss | -80.9328 |
| avg_hold_time_bars | 40.7678 |
| exposure | 0.6752 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
