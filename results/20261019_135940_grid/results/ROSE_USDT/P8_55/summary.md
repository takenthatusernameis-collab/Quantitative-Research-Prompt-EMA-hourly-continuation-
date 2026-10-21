# EMA Hourly Continuation — ROSE/USDT P8_55

**Symbol:** ROSE/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1085 |
| net_profit_factor | 0.6704 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 1.0361 |
| gross_win_rate | 0.4876 |
| sharpe_ratio | -5.1883 |
| sortino_ratio | -2.3970 |
| max_drawdown | 0.9489 |
| cagr | -0.6851 |
| net_avg_win | 37.0361 |
| net_avg_loss | -50.6580 |
| avg_hold_time_bars | 10.1889 |
| exposure | 0.5025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
