# EMA Hourly Continuation — GRAM/USDT P8_21

**Symbol:** GRAM/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1718 |
| net_profit_factor | 0.3206 |
| net_win_rate | 0.3888 |
| gross_profit_factor | 0.8102 |
| gross_win_rate | 0.4307 |
| sharpe_ratio | -15.5139 |
| sortino_ratio | -9.1985 |
| max_drawdown | 1.0000 |
| cagr | -0.9921 |
| net_avg_win | 7.0655 |
| net_avg_loss | -14.0188 |
| avg_hold_time_bars | 2.7672 |
| exposure | 0.2161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
