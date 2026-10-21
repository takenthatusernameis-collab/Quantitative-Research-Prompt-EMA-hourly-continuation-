# EMA Hourly Continuation — DASH/USDT P8_200

**Symbol:** DASH/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 209 |
| net_profit_factor | 0.7315 |
| net_win_rate | 0.4689 |
| gross_profit_factor | 0.8725 |
| gross_win_rate | 0.4689 |
| sharpe_ratio | -1.3502 |
| sortino_ratio | -0.2774 |
| max_drawdown | 0.3046 |
| cagr | -0.1205 |
| net_avg_win | 76.6229 |
| net_avg_loss | -92.4829 |
| avg_hold_time_bars | 87.1722 |
| exposure | 0.8281 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
