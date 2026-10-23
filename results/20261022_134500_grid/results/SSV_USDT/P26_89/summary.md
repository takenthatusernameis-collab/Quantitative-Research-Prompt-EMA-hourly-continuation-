# EMA Hourly Continuation — SSV/USDT P26_89

**Symbol:** SSV/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 733 |
| net_profit_factor | 0.5862 |
| net_win_rate | 0.4570 |
| gross_profit_factor | 0.8694 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -4.7439 |
| sortino_ratio | -1.8138 |
| max_drawdown | 0.8941 |
| cagr | -0.5764 |
| net_avg_win | 37.4482 |
| net_avg_loss | -53.7684 |
| avg_hold_time_bars | 9.8254 |
| exposure | 0.3259 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
