# EMA Hourly Continuation — DEGEN/USDT P21_89

**Symbol:** DEGEN/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.9148 |
| net_win_rate | 0.5188 |
| gross_profit_factor | 1.0821 |
| gross_win_rate | 0.5188 |
| sharpe_ratio | -0.6611 |
| sortino_ratio | -0.2084 |
| max_drawdown | 0.3534 |
| cagr | -0.0962 |
| net_avg_win | 96.6196 |
| net_avg_loss | -113.8488 |
| avg_hold_time_bars | 17.0146 |
| exposure | 0.3718 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
