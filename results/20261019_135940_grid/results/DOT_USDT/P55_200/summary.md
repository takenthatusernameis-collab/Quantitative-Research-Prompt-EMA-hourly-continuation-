# EMA Hourly Continuation — DOT/USDT P55_200

**Symbol:** DOT/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.6774 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 1.0066 |
| gross_win_rate | 0.5014 |
| sharpe_ratio | -2.3122 |
| sortino_ratio | -0.6116 |
| max_drawdown | 0.5251 |
| cagr | -0.2546 |
| net_avg_win | 62.6258 |
| net_avg_loss | -90.8886 |
| avg_hold_time_bars | 21.7734 |
| exposure | 0.3494 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
