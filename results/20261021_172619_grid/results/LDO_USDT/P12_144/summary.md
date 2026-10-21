# EMA Hourly Continuation — LDO/USDT P12_144

**Symbol:** LDO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.8139 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9471 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -1.1313 |
| sortino_ratio | -0.2972 |
| max_drawdown | 0.3112 |
| cagr | -0.1296 |
| net_avg_win | 77.5459 |
| net_avg_loss | -91.4184 |
| avg_hold_time_bars | 44.8879 |
| exposure | 0.6917 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
