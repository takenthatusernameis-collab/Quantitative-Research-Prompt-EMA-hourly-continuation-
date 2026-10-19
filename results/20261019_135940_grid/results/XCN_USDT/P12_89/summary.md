# EMA Hourly Continuation — XCN/USDT P12_89

**Symbol:** XCN/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 939 |
| net_profit_factor | 0.4382 |
| net_win_rate | 0.4217 |
| gross_profit_factor | 0.7444 |
| gross_win_rate | 0.4292 |
| sharpe_ratio | -7.9018 |
| sortino_ratio | -3.3850 |
| max_drawdown | 0.9866 |
| cagr | -0.8181 |
| net_avg_win | 19.4208 |
| net_avg_loss | -32.3246 |
| avg_hold_time_bars | 11.7401 |
| exposure | 0.5011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
