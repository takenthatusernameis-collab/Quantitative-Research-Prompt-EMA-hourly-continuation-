# EMA Hourly Continuation — METIS/USDT P50_55

**Symbol:** METIS/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 132 |
| net_profit_factor | 0.4940 |
| net_win_rate | 0.4015 |
| gross_profit_factor | 0.6874 |
| gross_win_rate | 0.4015 |
| sharpe_ratio | -2.5858 |
| sortino_ratio | -0.4225 |
| max_drawdown | 0.4010 |
| cagr | -0.1786 |
| net_avg_win | 71.8373 |
| net_avg_loss | -97.5515 |
| avg_hold_time_bars | 4.8561 |
| exposure | 0.0291 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
