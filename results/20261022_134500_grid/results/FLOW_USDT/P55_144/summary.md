# EMA Hourly Continuation — FLOW/USDT P55_144

**Symbol:** FLOW/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.5706 |
| net_win_rate | 0.4566 |
| gross_profit_factor | 0.8575 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -3.9168 |
| sortino_ratio | -1.2335 |
| max_drawdown | 0.7731 |
| cagr | -0.4420 |
| net_avg_win | 45.2141 |
| net_avg_loss | -66.5711 |
| avg_hold_time_bars | 12.2626 |
| exposure | 0.2759 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
