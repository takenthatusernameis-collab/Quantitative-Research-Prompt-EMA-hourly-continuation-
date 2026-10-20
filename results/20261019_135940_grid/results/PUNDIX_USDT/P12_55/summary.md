# EMA Hourly Continuation — PUNDIX/USDT P12_55

**Symbol:** PUNDIX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 995 |
| net_profit_factor | 0.5034 |
| net_win_rate | 0.4462 |
| gross_profit_factor | 0.8813 |
| gross_win_rate | 0.4633 |
| sharpe_ratio | -6.9499 |
| sortino_ratio | -3.0893 |
| max_drawdown | 0.9770 |
| cagr | -0.7759 |
| net_avg_win | 22.2995 |
| net_avg_loss | -35.6935 |
| avg_hold_time_bars | 8.8945 |
| exposure | 0.4023 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
