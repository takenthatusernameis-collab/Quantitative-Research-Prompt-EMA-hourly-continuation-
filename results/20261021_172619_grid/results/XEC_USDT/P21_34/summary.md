# EMA Hourly Continuation — XEC/USDT P21_34

**Symbol:** XEC/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.6193 |
| net_win_rate | 0.4925 |
| gross_profit_factor | 0.9827 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -3.3269 |
| sortino_ratio | -1.0315 |
| max_drawdown | 0.7116 |
| cagr | -0.3744 |
| net_avg_win | 49.2829 |
| net_avg_loss | -77.2174 |
| avg_hold_time_bars | 5.1785 |
| exposure | 0.1090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
