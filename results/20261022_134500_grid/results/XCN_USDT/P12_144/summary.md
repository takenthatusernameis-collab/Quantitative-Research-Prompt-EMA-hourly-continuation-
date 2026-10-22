# EMA Hourly Continuation — XCN/USDT P12_144

**Symbol:** XCN/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 707 |
| net_profit_factor | 0.5225 |
| net_win_rate | 0.4215 |
| gross_profit_factor | 0.8170 |
| gross_win_rate | 0.4399 |
| sharpe_ratio | -6.1966 |
| sortino_ratio | -2.3016 |
| max_drawdown | 0.9423 |
| cagr | -0.6774 |
| net_avg_win | 34.5747 |
| net_avg_loss | -48.2140 |
| avg_hold_time_bars | 19.1754 |
| exposure | 0.6162 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
