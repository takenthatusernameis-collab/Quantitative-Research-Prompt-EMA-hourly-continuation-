# EMA Hourly Continuation — FLUX/USDT P26_50

**Symbol:** FLUX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.6915 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9384 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -2.3827 |
| sortino_ratio | -0.6693 |
| max_drawdown | 0.5596 |
| cagr | -0.2641 |
| net_avg_win | 65.0576 |
| net_avg_loss | -87.0278 |
| avg_hold_time_bars | 5.5013 |
| exposure | 0.0963 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
