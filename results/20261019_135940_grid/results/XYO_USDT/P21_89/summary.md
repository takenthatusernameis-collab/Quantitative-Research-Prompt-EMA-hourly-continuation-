# EMA Hourly Continuation — XYO/USDT P21_89

**Symbol:** XYO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 836 |
| net_profit_factor | 0.4525 |
| net_win_rate | 0.4115 |
| gross_profit_factor | 0.7835 |
| gross_win_rate | 0.4258 |
| sharpe_ratio | -7.8368 |
| sortino_ratio | -3.1789 |
| max_drawdown | 0.9820 |
| cagr | -0.7944 |
| net_avg_win | 23.5839 |
| net_avg_loss | -36.4389 |
| avg_hold_time_bars | 9.7285 |
| exposure | 0.3680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
