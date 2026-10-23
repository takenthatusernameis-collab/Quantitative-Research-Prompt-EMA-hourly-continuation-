# EMA Hourly Continuation — TNSR/USDT P12_144

**Symbol:** TNSR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.6759 |
| net_win_rate | 0.4578 |
| gross_profit_factor | 0.9163 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -3.3067 |
| sortino_ratio | -1.0464 |
| max_drawdown | 0.7301 |
| cagr | -0.3905 |
| net_avg_win | 63.8180 |
| net_avg_loss | -79.7129 |
| avg_hold_time_bars | 29.1297 |
| exposure | 0.6710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
