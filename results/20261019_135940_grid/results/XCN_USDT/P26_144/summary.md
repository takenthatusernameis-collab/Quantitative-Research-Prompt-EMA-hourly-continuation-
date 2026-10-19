# EMA Hourly Continuation — XCN/USDT P26_144

**Symbol:** XCN/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 639 |
| net_profit_factor | 0.5313 |
| net_win_rate | 0.4460 |
| gross_profit_factor | 0.8518 |
| gross_win_rate | 0.4538 |
| sharpe_ratio | -5.1311 |
| sortino_ratio | -1.8138 |
| max_drawdown | 0.8929 |
| cagr | -0.5887 |
| net_avg_win | 35.5030 |
| net_avg_loss | -53.7975 |
| avg_hold_time_bars | 15.9624 |
| exposure | 0.4636 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
