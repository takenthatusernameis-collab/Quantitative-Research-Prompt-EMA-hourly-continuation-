# EMA Hourly Continuation — XPR/USDT P20_100

**Symbol:** XPR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.7030 |
| net_win_rate | 0.4684 |
| gross_profit_factor | 0.8866 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -2.3543 |
| sortino_ratio | -0.6797 |
| max_drawdown | 0.5535 |
| cagr | -0.2687 |
| net_avg_win | 66.7505 |
| net_avg_loss | -83.6782 |
| avg_hold_time_bars | 15.7282 |
| exposure | 0.2945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
