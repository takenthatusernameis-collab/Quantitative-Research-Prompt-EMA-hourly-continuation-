# EMA Hourly Continuation — CPOOL/USDT P50_200

**Symbol:** CPOOL/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.5641 |
| net_win_rate | 0.4187 |
| gross_profit_factor | 0.7768 |
| gross_win_rate | 0.4246 |
| sharpe_ratio | -4.6753 |
| sortino_ratio | -1.4628 |
| max_drawdown | 0.8437 |
| cagr | -0.5102 |
| net_avg_win | 51.1170 |
| net_avg_loss | -65.2555 |
| avg_hold_time_bars | 13.8234 |
| exposure | 0.3167 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
