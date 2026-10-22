# EMA Hourly Continuation — XRP/USDT P26_34

**Symbol:** XRP/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1119 |
| net_profit_factor | 0.1259 |
| net_win_rate | 0.3056 |
| gross_profit_factor | 0.6793 |
| gross_win_rate | 0.4004 |
| sharpe_ratio | -16.8630 |
| sortino_ratio | -8.5914 |
| max_drawdown | 1.0000 |
| cagr | -0.9914 |
| net_avg_win | 4.2111 |
| net_avg_loss | -14.7235 |
| avg_hold_time_bars | 1.8088 |
| exposure | 0.0920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
