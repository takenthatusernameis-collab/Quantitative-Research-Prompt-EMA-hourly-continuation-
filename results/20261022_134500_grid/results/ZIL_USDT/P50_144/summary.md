# EMA Hourly Continuation — ZIL/USDT P50_144

**Symbol:** ZIL/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.5704 |
| net_win_rate | 0.4652 |
| gross_profit_factor | 0.9146 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -3.6838 |
| sortino_ratio | -1.1732 |
| max_drawdown | 0.7531 |
| cagr | -0.4231 |
| net_avg_win | 42.4834 |
| net_avg_loss | -64.7896 |
| avg_hold_time_bars | 14.1849 |
| exposure | 0.3243 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
