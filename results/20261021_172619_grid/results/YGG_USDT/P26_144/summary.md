# EMA Hourly Continuation — YGG/USDT P26_144

**Symbol:** YGG/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.8458 |
| net_win_rate | 0.5038 |
| gross_profit_factor | 1.0225 |
| gross_win_rate | 0.5038 |
| sharpe_ratio | -1.1159 |
| sortino_ratio | -0.3184 |
| max_drawdown | 0.3777 |
| cagr | -0.1386 |
| net_avg_win | 85.6272 |
| net_avg_loss | -102.7684 |
| avg_hold_time_bars | 25.5890 |
| exposure | 0.4620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
