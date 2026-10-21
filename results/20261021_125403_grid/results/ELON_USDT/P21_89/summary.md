# EMA Hourly Continuation — ELON/USDT P21_89

**Symbol:** ELON/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.6934 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.8901 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -2.6831 |
| sortino_ratio | -0.8417 |
| max_drawdown | 0.6353 |
| cagr | -0.3207 |
| net_avg_win | 61.9150 |
| net_avg_loss | -78.5610 |
| avg_hold_time_bars | 13.6495 |
| exposure | 0.3009 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
