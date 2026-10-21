# EMA Hourly Continuation — VELO/USDT P26_89

**Symbol:** VELO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.8611 |
| net_win_rate | 0.5113 |
| gross_profit_factor | 1.0274 |
| gross_win_rate | 0.5113 |
| sharpe_ratio | -0.8962 |
| sortino_ratio | -0.2703 |
| max_drawdown | 0.3340 |
| cagr | -0.1200 |
| net_avg_win | 75.3234 |
| net_avg_loss | -91.5239 |
| avg_hold_time_bars | 14.2466 |
| exposure | 0.2862 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
