# EMA Hourly Continuation — TIA/USDT P50_144

**Symbol:** TIA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.8279 |
| net_win_rate | 0.4954 |
| gross_profit_factor | 0.9731 |
| gross_win_rate | 0.4954 |
| sharpe_ratio | -1.0352 |
| sortino_ratio | -0.2660 |
| max_drawdown | 0.2915 |
| cagr | -0.1169 |
| net_avg_win | 80.5970 |
| net_avg_loss | -95.5613 |
| avg_hold_time_bars | 18.6037 |
| exposure | 0.2731 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
