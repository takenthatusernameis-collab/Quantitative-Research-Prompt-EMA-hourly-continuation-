# EMA Hourly Continuation — ZK/USDT P26_144

**Symbol:** ZK/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.8047 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 0.9538 |
| gross_win_rate | 0.4874 |
| sharpe_ratio | -1.4298 |
| sortino_ratio | -0.4214 |
| max_drawdown | 0.3881 |
| cagr | -0.1780 |
| net_avg_win | 78.1752 |
| net_avg_loss | -92.3815 |
| avg_hold_time_bars | 22.9573 |
| exposure | 0.4455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
