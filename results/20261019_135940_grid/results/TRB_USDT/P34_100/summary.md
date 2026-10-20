# EMA Hourly Continuation — TRB/USDT P34_100

**Symbol:** TRB/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.4547 |
| net_win_rate | 0.4231 |
| gross_profit_factor | 0.7392 |
| gross_win_rate | 0.4407 |
| sharpe_ratio | -6.1866 |
| sortino_ratio | -2.2742 |
| max_drawdown | 0.9386 |
| cagr | -0.6668 |
| net_avg_win | 27.0490 |
| net_avg_loss | -43.6351 |
| avg_hold_time_bars | 9.3353 |
| exposure | 0.2885 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
