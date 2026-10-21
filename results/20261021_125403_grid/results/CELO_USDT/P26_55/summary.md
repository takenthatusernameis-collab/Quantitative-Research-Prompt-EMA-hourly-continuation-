# EMA Hourly Continuation — CELO/USDT P26_55

**Symbol:** CELO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.6990 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 0.9597 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -2.4392 |
| sortino_ratio | -0.7793 |
| max_drawdown | 0.5985 |
| cagr | -0.2997 |
| net_avg_win | 55.9737 |
| net_avg_loss | -77.8619 |
| avg_hold_time_bars | 7.2425 |
| exposure | 0.1635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
