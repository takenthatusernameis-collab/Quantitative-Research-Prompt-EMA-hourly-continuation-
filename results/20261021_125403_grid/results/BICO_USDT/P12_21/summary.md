# EMA Hourly Continuation — BICO/USDT P12_21

**Symbol:** BICO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 570 |
| net_profit_factor | 0.7063 |
| net_win_rate | 0.5035 |
| gross_profit_factor | 1.0178 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -2.6503 |
| sortino_ratio | -0.9094 |
| max_drawdown | 0.6505 |
| cagr | -0.3397 |
| net_avg_win | 54.2444 |
| net_avg_loss | -77.8876 |
| avg_hold_time_bars | 4.8018 |
| exposure | 0.1244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
