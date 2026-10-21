# EMA Hourly Continuation — FLR/USDT P12_144

**Symbol:** FLR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.7528 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 0.9484 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -1.8971 |
| sortino_ratio | -0.6026 |
| max_drawdown | 0.5194 |
| cagr | -0.2427 |
| net_avg_win | 63.2352 |
| net_avg_loss | -80.3477 |
| avg_hold_time_bars | 25.1030 |
| exposure | 0.5648 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
