# EMA Hourly Continuation — XCN/USDT P34_144

**Symbol:** XCN/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.7247 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.9170 |
| gross_win_rate | 0.4772 |
| sharpe_ratio | -2.0343 |
| sortino_ratio | -0.5592 |
| max_drawdown | 0.4759 |
| cagr | -0.2267 |
| net_avg_win | 70.7401 |
| net_avg_loss | -88.1502 |
| avg_hold_time_bars | 22.5040 |
| exposure | 0.3815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
