# EMA Hourly Continuation — RUNE/USDT P50_200

**Symbol:** RUNE/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.8114 |
| net_win_rate | 0.5340 |
| gross_profit_factor | 1.1410 |
| gross_win_rate | 0.5374 |
| sharpe_ratio | -1.0055 |
| sortino_ratio | -0.2429 |
| max_drawdown | 0.3835 |
| cagr | -0.1120 |
| net_avg_win | 70.6607 |
| net_avg_loss | -99.8003 |
| avg_hold_time_bars | 36.8844 |
| exposure | 0.4929 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
