# EMA Hourly Continuation — AMP/USDT P26_200

**Symbol:** AMP/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.6066 |
| net_win_rate | 0.4366 |
| gross_profit_factor | 0.7667 |
| gross_win_rate | 0.4366 |
| sharpe_ratio | -3.1309 |
| sortino_ratio | -0.9143 |
| max_drawdown | 0.6720 |
| cagr | -0.3445 |
| net_avg_win | 54.1964 |
| net_avg_loss | -69.2447 |
| avg_hold_time_bars | 27.4272 |
| exposure | 0.5311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
