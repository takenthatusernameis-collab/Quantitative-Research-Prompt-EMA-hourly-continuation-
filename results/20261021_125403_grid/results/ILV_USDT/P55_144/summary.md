# EMA Hourly Continuation — ILV/USDT P55_144

**Symbol:** ILV/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.8464 |
| net_win_rate | 0.5174 |
| gross_profit_factor | 1.0685 |
| gross_win_rate | 0.5174 |
| sharpe_ratio | -0.9662 |
| sortino_ratio | -0.2578 |
| max_drawdown | 0.2942 |
| cagr | -0.1130 |
| net_avg_win | 80.5396 |
| net_avg_loss | -102.0309 |
| avg_hold_time_bars | 16.2733 |
| exposure | 0.2545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
