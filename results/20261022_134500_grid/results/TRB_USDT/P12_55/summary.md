# EMA Hourly Continuation — TRB/USDT P12_55

**Symbol:** TRB/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1053 |
| net_profit_factor | 0.5114 |
| net_win_rate | 0.4406 |
| gross_profit_factor | 0.8580 |
| gross_win_rate | 0.4549 |
| sharpe_ratio | -7.5076 |
| sortino_ratio | -3.4018 |
| max_drawdown | 0.9856 |
| cagr | -0.8132 |
| net_avg_win | 22.2331 |
| net_avg_loss | -34.2461 |
| avg_hold_time_bars | 8.0389 |
| exposure | 0.3830 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
