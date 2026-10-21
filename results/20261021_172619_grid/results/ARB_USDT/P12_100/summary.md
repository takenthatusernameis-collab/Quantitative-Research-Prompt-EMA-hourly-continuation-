# EMA Hourly Continuation — ARB/USDT P12_100

**Symbol:** ARB/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.9026 |
| net_win_rate | 0.5272 |
| gross_profit_factor | 1.0994 |
| gross_win_rate | 0.5272 |
| sharpe_ratio | -0.5756 |
| sortino_ratio | -0.1706 |
| max_drawdown | 0.2522 |
| cagr | -0.0799 |
| net_avg_win | 78.4263 |
| net_avg_loss | -96.8841 |
| avg_hold_time_bars | 30.1466 |
| exposure | 0.5796 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
