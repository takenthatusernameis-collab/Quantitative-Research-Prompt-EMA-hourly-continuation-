# EMA Hourly Continuation — AVA/USDT P26_34

**Symbol:** AVA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1028 |
| net_profit_factor | 0.1948 |
| net_win_rate | 0.3988 |
| gross_profit_factor | 0.6540 |
| gross_win_rate | 0.4426 |
| sharpe_ratio | -12.0465 |
| sortino_ratio | -5.5755 |
| max_drawdown | 0.9994 |
| cagr | -0.9457 |
| net_avg_win | 5.8975 |
| net_avg_loss | -20.0831 |
| avg_hold_time_bars | 2.1634 |
| exposure | 0.1011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
