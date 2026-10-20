# EMA Hourly Continuation — PUNDIX/USDT P12_34

**Symbol:** PUNDIX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1200 |
| net_profit_factor | 0.3748 |
| net_win_rate | 0.4242 |
| gross_profit_factor | 0.7748 |
| gross_win_rate | 0.4467 |
| sharpe_ratio | -9.5794 |
| sortino_ratio | -4.6802 |
| max_drawdown | 0.9972 |
| cagr | -0.9017 |
| net_avg_win | 11.7424 |
| net_avg_loss | -23.0787 |
| avg_hold_time_bars | 5.4308 |
| exposure | 0.2962 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
