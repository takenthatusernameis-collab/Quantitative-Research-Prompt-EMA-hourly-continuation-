# EMA Hourly Continuation — AUCTION/USDT P34_144

**Symbol:** AUCTION/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.7157 |
| net_win_rate | 0.4826 |
| gross_profit_factor | 0.9792 |
| gross_win_rate | 0.4848 |
| sharpe_ratio | -2.6995 |
| sortino_ratio | -0.8148 |
| max_drawdown | 0.6423 |
| cagr | -0.3210 |
| net_avg_win | 70.6887 |
| net_avg_loss | -92.1243 |
| avg_hold_time_bars | 17.6957 |
| exposure | 0.3684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
