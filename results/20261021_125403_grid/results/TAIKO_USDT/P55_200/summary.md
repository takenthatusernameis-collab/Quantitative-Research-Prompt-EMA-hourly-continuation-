# EMA Hourly Continuation — TAIKO/USDT P55_200

**Symbol:** TAIKO/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.7241 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.9086 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -1.7109 |
| sortino_ratio | -0.4002 |
| max_drawdown | 0.3678 |
| cagr | -0.1677 |
| net_avg_win | 76.6802 |
| net_avg_loss | -95.6191 |
| avg_hold_time_bars | 30.3412 |
| exposure | 0.3716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
