# EMA Hourly Continuation — ASTR/USDT P12_200

**Symbol:** ASTR/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.9006 |
| net_win_rate | 0.5365 |
| gross_profit_factor | 1.2432 |
| gross_win_rate | 0.5547 |
| sharpe_ratio | -0.5000 |
| sortino_ratio | -0.1185 |
| max_drawdown | 0.2280 |
| cagr | -0.0561 |
| net_avg_win | 83.5808 |
| net_avg_loss | -107.4170 |
| avg_hold_time_bars | 64.5839 |
| exposure | 0.8008 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
