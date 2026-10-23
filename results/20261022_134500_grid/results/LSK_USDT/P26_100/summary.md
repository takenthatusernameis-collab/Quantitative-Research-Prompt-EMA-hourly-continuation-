# EMA Hourly Continuation — LSK/USDT P26_100

**Symbol:** LSK/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 583 |
| net_profit_factor | 0.6182 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.9566 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -3.7769 |
| sortino_ratio | -1.2820 |
| max_drawdown | 0.8044 |
| cagr | -0.4606 |
| net_avg_win | 46.0402 |
| net_avg_loss | -67.4210 |
| avg_hold_time_bars | 13.3551 |
| exposure | 0.3539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
