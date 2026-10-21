# EMA Hourly Continuation — XCN/USDT P12_100

**Symbol:** XCN/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.7228 |
| net_win_rate | 0.4734 |
| gross_profit_factor | 0.8968 |
| gross_win_rate | 0.4734 |
| sharpe_ratio | -2.3518 |
| sortino_ratio | -0.7535 |
| max_drawdown | 0.5964 |
| cagr | -0.2938 |
| net_avg_win | 63.3039 |
| net_avg_loss | -78.7222 |
| avg_hold_time_bars | 21.0966 |
| exposure | 0.4862 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
