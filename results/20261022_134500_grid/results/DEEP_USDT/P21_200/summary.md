# EMA Hourly Continuation — DEEP/USDT P21_200

**Symbol:** DEEP/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 256 |
| net_profit_factor | 0.7097 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9040 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -1.8753 |
| sortino_ratio | -0.4705 |
| max_drawdown | 0.3740 |
| cagr | -0.2009 |
| net_avg_win | 72.9033 |
| net_avg_loss | -93.5241 |
| avg_hold_time_bars | 46.0859 |
| exposure | 0.6680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
