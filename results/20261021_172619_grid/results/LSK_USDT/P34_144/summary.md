# EMA Hourly Continuation — LSK/USDT P34_144

**Symbol:** LSK/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.7504 |
| net_win_rate | 0.4945 |
| gross_profit_factor | 0.9657 |
| gross_win_rate | 0.4945 |
| sharpe_ratio | -1.6593 |
| sortino_ratio | -0.4531 |
| max_drawdown | 0.5060 |
| cagr | -0.1896 |
| net_avg_win | 68.1186 |
| net_avg_loss | -88.8153 |
| avg_hold_time_bars | 24.5410 |
| exposure | 0.4083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
