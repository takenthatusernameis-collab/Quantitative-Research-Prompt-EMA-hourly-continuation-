# EMA Hourly Continuation — COTI/USDT P21_89

**Symbol:** COTI/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 761 |
| net_profit_factor | 0.6921 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 1.0159 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -3.5075 |
| sortino_ratio | -1.3656 |
| max_drawdown | 0.8135 |
| cagr | -0.4786 |
| net_avg_win | 48.3926 |
| net_avg_loss | -67.5706 |
| avg_hold_time_bars | 10.7477 |
| exposure | 0.3718 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
