# EMA Hourly Continuation — HTR/USDT P55_89

**Symbol:** HTR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 745 |
| net_profit_factor | 0.3933 |
| net_win_rate | 0.3839 |
| gross_profit_factor | 0.6718 |
| gross_win_rate | 0.4040 |
| sharpe_ratio | -8.5617 |
| sortino_ratio | -3.2889 |
| max_drawdown | 0.9858 |
| cagr | -0.8110 |
| net_avg_win | 22.3189 |
| net_avg_loss | -35.3613 |
| avg_hold_time_bars | 4.4107 |
| exposure | 0.1494 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
