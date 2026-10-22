# EMA Hourly Continuation — AVAX/USDT P26_34

**Symbol:** AVAX/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1024 |
| net_profit_factor | 0.3228 |
| net_win_rate | 0.3730 |
| gross_profit_factor | 0.9484 |
| gross_win_rate | 0.4180 |
| sharpe_ratio | -12.9531 |
| sortino_ratio | -6.0147 |
| max_drawdown | 0.9997 |
| cagr | -0.9596 |
| net_avg_win | 12.4735 |
| net_avg_loss | -22.9934 |
| avg_hold_time_bars | 1.8506 |
| exposure | 0.0861 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
