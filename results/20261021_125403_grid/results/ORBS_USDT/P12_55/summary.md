# EMA Hourly Continuation — ORBS/USDT P12_55

**Symbol:** ORBS/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 700 |
| net_profit_factor | 0.5794 |
| net_win_rate | 0.4314 |
| gross_profit_factor | 0.8039 |
| gross_win_rate | 0.4329 |
| sharpe_ratio | -5.1373 |
| sortino_ratio | -1.9315 |
| max_drawdown | 0.8956 |
| cagr | -0.5902 |
| net_avg_win | 40.7598 |
| net_avg_loss | -53.3797 |
| avg_hold_time_bars | 11.6771 |
| exposure | 0.3715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
