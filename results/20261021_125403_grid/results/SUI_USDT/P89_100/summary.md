# EMA Hourly Continuation — SUI/USDT P89_100

**Symbol:** SUI/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 72 |
| net_profit_factor | 0.5781 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.7766 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -1.3624 |
| sortino_ratio | -0.1647 |
| max_drawdown | 0.1911 |
| cagr | -0.0729 |
| net_avg_win | 74.0810 |
| net_avg_loss | -102.5224 |
| avg_hold_time_bars | 5.3611 |
| exposure | 0.0175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
