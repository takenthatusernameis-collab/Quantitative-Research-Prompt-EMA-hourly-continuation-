# EMA Hourly Continuation — LUNA/USDT P8_20

**Symbol:** LUNA/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.6829 |
| net_win_rate | 0.4872 |
| gross_profit_factor | 0.9467 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -2.4810 |
| sortino_ratio | -0.7369 |
| max_drawdown | 0.5852 |
| cagr | -0.2864 |
| net_avg_win | 58.8847 |
| net_avg_loss | -81.9136 |
| avg_hold_time_bars | 5.8392 |
| exposure | 0.1139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
