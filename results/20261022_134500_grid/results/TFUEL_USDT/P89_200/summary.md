# EMA Hourly Continuation — TFUEL/USDT P89_200

**Symbol:** TFUEL/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.4354 |
| net_win_rate | 0.3845 |
| gross_profit_factor | 0.7568 |
| gross_win_rate | 0.3981 |
| sharpe_ratio | -6.7803 |
| sortino_ratio | -2.1673 |
| max_drawdown | 0.9357 |
| cagr | -0.6605 |
| net_avg_win | 36.3926 |
| net_avg_loss | -52.2093 |
| avg_hold_time_bars | 8.1146 |
| exposure | 0.1891 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
