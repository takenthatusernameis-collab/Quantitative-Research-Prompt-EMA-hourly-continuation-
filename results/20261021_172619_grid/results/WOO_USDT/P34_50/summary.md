# EMA Hourly Continuation — WOO/USDT P34_50

**Symbol:** WOO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.6377 |
| net_win_rate | 0.4689 |
| gross_profit_factor | 0.8964 |
| gross_win_rate | 0.4689 |
| sharpe_ratio | -2.7784 |
| sortino_ratio | -0.7477 |
| max_drawdown | 0.5929 |
| cagr | -0.2899 |
| net_avg_win | 61.1533 |
| net_avg_loss | -84.6731 |
| avg_hold_time_bars | 5.5763 |
| exposure | 0.0897 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
