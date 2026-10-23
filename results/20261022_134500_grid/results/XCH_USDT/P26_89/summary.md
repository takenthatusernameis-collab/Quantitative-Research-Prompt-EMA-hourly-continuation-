# EMA Hourly Continuation — XCH/USDT P26_89

**Symbol:** XCH/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 818 |
| net_profit_factor | 0.4976 |
| net_win_rate | 0.4633 |
| gross_profit_factor | 0.8853 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -5.3027 |
| sortino_ratio | -2.1272 |
| max_drawdown | 0.9251 |
| cagr | -0.6425 |
| net_avg_win | 24.1618 |
| net_avg_loss | -41.9174 |
| avg_hold_time_bars | 9.1687 |
| exposure | 0.3409 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
