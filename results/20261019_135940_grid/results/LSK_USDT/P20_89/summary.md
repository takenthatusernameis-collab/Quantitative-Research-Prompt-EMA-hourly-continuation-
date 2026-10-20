# EMA Hourly Continuation — LSK/USDT P20_89

**Symbol:** LSK/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.5808 |
| net_win_rate | 0.4592 |
| gross_profit_factor | 0.8928 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -4.3619 |
| sortino_ratio | -1.5640 |
| max_drawdown | 0.8557 |
| cagr | -0.5262 |
| net_avg_win | 39.3735 |
| net_avg_loss | -57.5534 |
| avg_hold_time_bars | 12.9076 |
| exposure | 0.3808 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
