# EMA Hourly Continuation — XCN/USDT P34_55

**Symbol:** XCN/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.5508 |
| net_win_rate | 0.4226 |
| gross_profit_factor | 0.7589 |
| gross_win_rate | 0.4226 |
| sharpe_ratio | -3.2105 |
| sortino_ratio | -0.7430 |
| max_drawdown | 0.5811 |
| cagr | -0.2903 |
| net_avg_win | 63.1925 |
| net_avg_loss | -83.9906 |
| avg_hold_time_bars | 6.4717 |
| exposure | 0.0780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
