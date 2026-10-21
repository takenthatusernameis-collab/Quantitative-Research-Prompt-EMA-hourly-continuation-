# EMA Hourly Continuation — DBR/USDT P8_26

**Symbol:** DBR/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.6929 |
| net_win_rate | 0.5035 |
| gross_profit_factor | 1.0683 |
| gross_win_rate | 0.5071 |
| sharpe_ratio | -3.5133 |
| sortino_ratio | -1.3361 |
| max_drawdown | 0.7422 |
| cagr | -0.4597 |
| net_avg_win | 56.1566 |
| net_avg_loss | -82.1997 |
| avg_hold_time_bars | 7.6749 |
| exposure | 0.2470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
