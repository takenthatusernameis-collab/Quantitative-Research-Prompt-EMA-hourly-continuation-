# EMA Hourly Continuation — UNI/USDT P21_144

**Symbol:** UNI/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.6359 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9542 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -3.2821 |
| sortino_ratio | -1.0201 |
| max_drawdown | 0.7191 |
| cagr | -0.3943 |
| net_avg_win | 51.8949 |
| net_avg_loss | -76.5261 |
| avg_hold_time_bars | 22.3916 |
| exposure | 0.5069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
