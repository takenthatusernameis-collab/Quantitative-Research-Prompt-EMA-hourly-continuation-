# EMA Hourly Continuation — FLUX/USDT P21_144

**Symbol:** FLUX/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.6883 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.9659 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -2.7682 |
| sortino_ratio | -0.8841 |
| max_drawdown | 0.6728 |
| cagr | -0.3392 |
| net_avg_win | 58.7709 |
| net_avg_loss | -78.2971 |
| avg_hold_time_bars | 23.5098 |
| exposure | 0.5429 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
