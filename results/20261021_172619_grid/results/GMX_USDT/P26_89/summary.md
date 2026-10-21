# EMA Hourly Continuation — GMX/USDT P26_89

**Symbol:** GMX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.6650 |
| net_win_rate | 0.4597 |
| gross_profit_factor | 0.8836 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -3.2576 |
| sortino_ratio | -1.0693 |
| max_drawdown | 0.7229 |
| cagr | -0.3876 |
| net_avg_win | 57.3773 |
| net_avg_loss | -73.3990 |
| avg_hold_time_bars | 11.7054 |
| exposure | 0.2836 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
