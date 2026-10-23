# EMA Hourly Continuation — TNSR/USDT P21_55

**Symbol:** TNSR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 890 |
| net_profit_factor | 0.6402 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 0.9719 |
| gross_win_rate | 0.4888 |
| sharpe_ratio | -4.8947 |
| sortino_ratio | -2.0588 |
| max_drawdown | 0.9211 |
| cagr | -0.6240 |
| net_avg_win | 38.3120 |
| net_avg_loss | -54.6974 |
| avg_hold_time_bars | 5.9955 |
| exposure | 0.2415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
