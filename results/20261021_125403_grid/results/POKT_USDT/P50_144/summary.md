# EMA Hourly Continuation — POKT/USDT P50_144

**Symbol:** POKT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.6879 |
| net_win_rate | 0.4528 |
| gross_profit_factor | 0.8750 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -2.7555 |
| sortino_ratio | -0.8026 |
| max_drawdown | 0.6231 |
| cagr | -0.3095 |
| net_avg_win | 69.6805 |
| net_avg_loss | -83.8348 |
| avg_hold_time_bars | 14.9151 |
| exposure | 0.2862 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
