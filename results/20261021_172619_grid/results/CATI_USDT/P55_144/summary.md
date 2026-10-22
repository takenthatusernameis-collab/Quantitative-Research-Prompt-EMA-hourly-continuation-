# EMA Hourly Continuation — CATI/USDT P55_144

**Symbol:** CATI/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.5504 |
| net_win_rate | 0.4106 |
| gross_profit_factor | 0.6918 |
| gross_win_rate | 0.4106 |
| sharpe_ratio | -3.3629 |
| sortino_ratio | -0.8449 |
| max_drawdown | 0.5701 |
| cagr | -0.3250 |
| net_avg_win | 63.3570 |
| net_avg_loss | -80.2020 |
| avg_hold_time_bars | 17.9734 |
| exposure | 0.2591 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
