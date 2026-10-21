# EMA Hourly Continuation — LDO/USDT P12_89

**Symbol:** LDO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.7948 |
| net_win_rate | 0.4865 |
| gross_profit_factor | 0.9410 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -1.5678 |
| sortino_ratio | -0.4905 |
| max_drawdown | 0.4448 |
| cagr | -0.2038 |
| net_avg_win | 72.1194 |
| net_avg_loss | -85.9669 |
| avg_hold_time_bars | 25.1019 |
| exposure | 0.5488 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
