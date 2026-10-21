# EMA Hourly Continuation — T/USDT P20_34

**Symbol:** T/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.6139 |
| net_win_rate | 0.4858 |
| gross_profit_factor | 1.0167 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -3.9176 |
| sortino_ratio | -1.2919 |
| max_drawdown | 0.7866 |
| cagr | -0.4462 |
| net_avg_win | 48.1269 |
| net_avg_loss | -74.0527 |
| avg_hold_time_bars | 6.1746 |
| exposure | 0.1473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
