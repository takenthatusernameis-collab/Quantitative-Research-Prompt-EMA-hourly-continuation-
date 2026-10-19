# EMA Hourly Continuation — SKY/USDT P21_34

**Symbol:** SKY/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 902 |
| net_profit_factor | 0.3428 |
| net_win_rate | 0.4135 |
| gross_profit_factor | 0.8191 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -10.7319 |
| sortino_ratio | -5.0801 |
| max_drawdown | 0.9949 |
| cagr | -0.9241 |
| net_avg_win | 13.9107 |
| net_avg_loss | -28.6157 |
| avg_hold_time_bars | 2.9922 |
| exposure | 0.1505 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
