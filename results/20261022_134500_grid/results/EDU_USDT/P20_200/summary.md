# EMA Hourly Continuation — EDU/USDT P20_200

**Symbol:** EDU/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.6888 |
| net_win_rate | 0.4634 |
| gross_profit_factor | 0.8917 |
| gross_win_rate | 0.4681 |
| sharpe_ratio | -2.5221 |
| sortino_ratio | -0.7262 |
| max_drawdown | 0.6007 |
| cagr | -0.2920 |
| net_avg_win | 65.6637 |
| net_avg_loss | -82.3146 |
| avg_hold_time_bars | 33.4468 |
| exposure | 0.6402 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
