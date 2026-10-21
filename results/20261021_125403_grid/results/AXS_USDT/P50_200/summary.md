# EMA Hourly Continuation — AXS/USDT P50_200

**Symbol:** AXS/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.9212 |
| net_win_rate | 0.5365 |
| gross_profit_factor | 1.1429 |
| gross_win_rate | 0.5365 |
| sharpe_ratio | -0.3648 |
| sortino_ratio | -0.0871 |
| max_drawdown | 0.1728 |
| cagr | -0.0425 |
| net_avg_win | 82.5097 |
| net_avg_loss | -103.6755 |
| avg_hold_time_bars | 30.6861 |
| exposure | 0.3805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
