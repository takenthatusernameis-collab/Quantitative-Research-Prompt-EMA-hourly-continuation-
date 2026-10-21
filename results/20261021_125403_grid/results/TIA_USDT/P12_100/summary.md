# EMA Hourly Continuation — TIA/USDT P12_100

**Symbol:** TIA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.8503 |
| net_win_rate | 0.4989 |
| gross_profit_factor | 0.9829 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -1.0301 |
| sortino_ratio | -0.3084 |
| max_drawdown | 0.3567 |
| cagr | -0.1350 |
| net_avg_win | 79.1839 |
| net_avg_loss | -92.7031 |
| avg_hold_time_bars | 28.2756 |
| exposure | 0.5642 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
