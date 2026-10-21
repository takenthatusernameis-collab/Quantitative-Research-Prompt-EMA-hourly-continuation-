# EMA Hourly Continuation — AXS/USDT P34_200

**Symbol:** AXS/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.9754 |
| net_win_rate | 0.5442 |
| gross_profit_factor | 1.1911 |
| gross_win_rate | 0.5476 |
| sharpe_ratio | -0.0806 |
| sortino_ratio | -0.0200 |
| max_drawdown | 0.1898 |
| cagr | -0.0144 |
| net_avg_win | 88.6683 |
| net_avg_loss | -108.5455 |
| avg_hold_time_bars | 37.3095 |
| exposure | 0.4964 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
