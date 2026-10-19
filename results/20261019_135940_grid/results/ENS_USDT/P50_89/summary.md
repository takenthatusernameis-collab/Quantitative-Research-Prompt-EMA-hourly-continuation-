# EMA Hourly Continuation — ENS/USDT P50_89

**Symbol:** ENS/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.4986 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.9060 |
| gross_win_rate | 0.4786 |
| sharpe_ratio | -6.0654 |
| sortino_ratio | -2.2511 |
| max_drawdown | 0.9424 |
| cagr | -0.6761 |
| net_avg_win | 29.0661 |
| net_avg_loss | -49.3943 |
| avg_hold_time_bars | 4.8932 |
| exposure | 0.1561 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
