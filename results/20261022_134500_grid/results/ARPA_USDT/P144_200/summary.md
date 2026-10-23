# EMA Hourly Continuation — ARPA/USDT P144_200

**Symbol:** ARPA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.4480 |
| net_win_rate | 0.4249 |
| gross_profit_factor | 0.8603 |
| gross_win_rate | 0.4442 |
| sharpe_ratio | -6.0168 |
| sortino_ratio | -1.8289 |
| max_drawdown | 0.9035 |
| cagr | -0.6022 |
| net_avg_win | 36.9870 |
| net_avg_loss | -60.9915 |
| avg_hold_time_bars | 5.0021 |
| exposure | 0.1055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
