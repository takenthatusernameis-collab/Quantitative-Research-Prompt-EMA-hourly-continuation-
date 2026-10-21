# EMA Hourly Continuation — SUN/USDT P8_89

**Symbol:** SUN/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.5955 |
| net_win_rate | 0.4481 |
| gross_profit_factor | 0.9221 |
| gross_win_rate | 0.4611 |
| sharpe_ratio | -4.7668 |
| sortino_ratio | -1.5625 |
| max_drawdown | 0.8607 |
| cagr | -0.5264 |
| net_avg_win | 51.5992 |
| net_avg_loss | -70.3676 |
| avg_hold_time_bars | 24.8481 |
| exposure | 0.6072 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
