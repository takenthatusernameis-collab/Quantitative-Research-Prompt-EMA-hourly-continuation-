# EMA Hourly Continuation — HNT/USDT P50_144

**Symbol:** HNT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 574 |
| net_profit_factor | 0.4524 |
| net_win_rate | 0.4077 |
| gross_profit_factor | 0.6368 |
| gross_win_rate | 0.4077 |
| sharpe_ratio | -5.3762 |
| sortino_ratio | -1.8072 |
| max_drawdown | 0.8940 |
| cagr | -0.5808 |
| net_avg_win | 31.3305 |
| net_avg_loss | -47.6610 |
| avg_hold_time_bars | 11.2282 |
| exposure | 0.2930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
