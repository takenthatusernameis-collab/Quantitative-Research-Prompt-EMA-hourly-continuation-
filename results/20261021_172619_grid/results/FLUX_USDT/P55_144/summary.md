# EMA Hourly Continuation — FLUX/USDT P55_144

**Symbol:** FLUX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.8864 |
| net_win_rate | 0.5322 |
| gross_profit_factor | 1.1214 |
| gross_win_rate | 0.5322 |
| sharpe_ratio | -0.6171 |
| sortino_ratio | -0.1647 |
| max_drawdown | 0.2038 |
| cagr | -0.0761 |
| net_avg_win | 77.3511 |
| net_avg_loss | -99.2594 |
| avg_hold_time_bars | 16.5205 |
| exposure | 0.2568 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
