# EMA Hourly Continuation — CELO/USDT P34_89

**Symbol:** CELO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.9280 |
| net_win_rate | 0.5475 |
| gross_profit_factor | 1.2100 |
| gross_win_rate | 0.5475 |
| sharpe_ratio | -0.4572 |
| sortino_ratio | -0.1390 |
| max_drawdown | 0.2738 |
| cagr | -0.0669 |
| net_avg_win | 85.4336 |
| net_avg_loss | -111.3908 |
| avg_hold_time_bars | 12.7873 |
| exposure | 0.2558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
