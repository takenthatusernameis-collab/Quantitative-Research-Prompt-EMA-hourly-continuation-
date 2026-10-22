# EMA Hourly Continuation — ACE/USDT P26_200

**Symbol:** ACE/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.8445 |
| net_win_rate | 0.5065 |
| gross_profit_factor | 1.0104 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -0.8702 |
| sortino_ratio | -0.2172 |
| max_drawdown | 0.2937 |
| cagr | -0.0970 |
| net_avg_win | 79.5223 |
| net_avg_loss | -96.6546 |
| avg_hold_time_bars | 40.9248 |
| exposure | 0.5667 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
