# EMA Hourly Continuation — OGN/USDT P50_144

**Symbol:** OGN/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 544 |
| net_profit_factor | 0.4570 |
| net_win_rate | 0.4210 |
| gross_profit_factor | 0.7435 |
| gross_win_rate | 0.4338 |
| sharpe_ratio | -5.4129 |
| sortino_ratio | -1.7652 |
| max_drawdown | 0.8889 |
| cagr | -0.5754 |
| net_avg_win | 32.5220 |
| net_avg_loss | -51.7322 |
| avg_hold_time_bars | 12.3824 |
| exposure | 0.3048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
