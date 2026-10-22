# EMA Hourly Continuation — OP/USDT P26_55

**Symbol:** OP/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 925 |
| net_profit_factor | 0.4815 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.9015 |
| gross_win_rate | 0.4681 |
| sharpe_ratio | -6.5985 |
| sortino_ratio | -2.8403 |
| max_drawdown | 0.9696 |
| cagr | -0.7463 |
| net_avg_win | 21.0066 |
| net_avg_loss | -37.5686 |
| avg_hold_time_bars | 4.0216 |
| exposure | 0.1691 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
