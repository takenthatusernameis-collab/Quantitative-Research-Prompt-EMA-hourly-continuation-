# EMA Hourly Continuation — EDU/USDT P21_89

**Symbol:** EDU/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.7931 |
| net_win_rate | 0.5035 |
| gross_profit_factor | 1.0003 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -1.6708 |
| sortino_ratio | -0.5742 |
| max_drawdown | 0.5070 |
| cagr | -0.2337 |
| net_avg_win | 64.4159 |
| net_avg_loss | -82.3542 |
| avg_hold_time_bars | 13.6090 |
| exposure | 0.3559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
