# EMA Hourly Continuation — LUNA/USDT P12_200

**Symbol:** LUNA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.7771 |
| net_win_rate | 0.4856 |
| gross_profit_factor | 0.9401 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -1.3850 |
| sortino_ratio | -0.3495 |
| max_drawdown | 0.3499 |
| cagr | -0.1497 |
| net_avg_win | 76.7362 |
| net_avg_loss | -93.2264 |
| avg_hold_time_bars | 49.4281 |
| exposure | 0.7032 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
