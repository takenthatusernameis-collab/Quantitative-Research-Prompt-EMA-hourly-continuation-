# EMA Hourly Continuation — YGG/USDT P50_89

**Symbol:** YGG/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.6334 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0471 |
| gross_win_rate | 0.5163 |
| sharpe_ratio | -3.8421 |
| sortino_ratio | -1.4133 |
| max_drawdown | 0.8277 |
| cagr | -0.4875 |
| net_avg_win | 41.6577 |
| net_avg_loss | -65.7649 |
| avg_hold_time_bars | 5.1243 |
| exposure | 0.1567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
