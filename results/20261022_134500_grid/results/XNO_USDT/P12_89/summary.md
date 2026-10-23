# EMA Hourly Continuation — XNO/USDT P12_89

**Symbol:** XNO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 924 |
| net_profit_factor | 0.5472 |
| net_win_rate | 0.4080 |
| gross_profit_factor | 0.8395 |
| gross_win_rate | 0.4177 |
| sharpe_ratio | -7.3188 |
| sortino_ratio | -3.1247 |
| max_drawdown | 0.9785 |
| cagr | -0.7803 |
| net_avg_win | 31.3384 |
| net_avg_loss | -39.4739 |
| avg_hold_time_bars | 11.7879 |
| exposure | 0.4951 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
