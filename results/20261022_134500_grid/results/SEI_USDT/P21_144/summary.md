# EMA Hourly Continuation — SEI/USDT P21_144

**Symbol:** SEI/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.7788 |
| net_win_rate | 0.5057 |
| gross_profit_factor | 1.0617 |
| gross_win_rate | 0.5147 |
| sharpe_ratio | -1.7556 |
| sortino_ratio | -0.5222 |
| max_drawdown | 0.4983 |
| cagr | -0.2194 |
| net_avg_win | 73.1493 |
| net_avg_loss | -96.0752 |
| avg_hold_time_bars | 28.5986 |
| exposure | 0.5733 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
