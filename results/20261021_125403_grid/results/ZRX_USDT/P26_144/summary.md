# EMA Hourly Continuation — ZRX/USDT P26_144

**Symbol:** ZRX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.8025 |
| net_win_rate | 0.5082 |
| gross_profit_factor | 1.0270 |
| gross_win_rate | 0.5082 |
| sharpe_ratio | -1.4052 |
| sortino_ratio | -0.4164 |
| max_drawdown | 0.4141 |
| cagr | -0.1750 |
| net_avg_win | 71.7494 |
| net_avg_loss | -92.3887 |
| avg_hold_time_bars | 23.5948 |
| exposure | 0.4580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
