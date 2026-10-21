# EMA Hourly Continuation — WOO/USDT P26_89

**Symbol:** WOO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.8077 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 1.0107 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -1.7065 |
| sortino_ratio | -0.5461 |
| max_drawdown | 0.5603 |
| cagr | -0.2234 |
| net_avg_win | 79.2667 |
| net_avg_loss | -97.3596 |
| avg_hold_time_bars | 13.5020 |
| exposure | 0.3069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
