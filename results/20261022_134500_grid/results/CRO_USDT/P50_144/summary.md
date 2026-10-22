# EMA Hourly Continuation — CRO/USDT P50_144

**Symbol:** CRO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.5615 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 1.0154 |
| gross_win_rate | 0.5020 |
| sharpe_ratio | -3.9713 |
| sortino_ratio | -1.2514 |
| max_drawdown | 0.7885 |
| cagr | -0.4534 |
| net_avg_win | 41.4703 |
| net_avg_loss | -69.2611 |
| avg_hold_time_bars | 13.1928 |
| exposure | 0.2986 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
