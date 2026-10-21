# EMA Hourly Continuation — CFG/USDT P12_200

**Symbol:** CFG/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 253 |
| net_profit_factor | 0.8220 |
| net_win_rate | 0.4862 |
| gross_profit_factor | 0.9339 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -0.8993 |
| sortino_ratio | -0.2040 |
| max_drawdown | 0.2543 |
| cagr | -0.0911 |
| net_avg_win | 80.1068 |
| net_avg_loss | -92.2067 |
| avg_hold_time_bars | 67.6364 |
| exposure | 0.7778 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
