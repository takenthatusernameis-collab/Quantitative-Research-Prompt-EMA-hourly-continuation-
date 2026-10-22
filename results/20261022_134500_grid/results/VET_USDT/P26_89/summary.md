# EMA Hourly Continuation — VET/USDT P26_89

**Symbol:** VET/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 727 |
| net_profit_factor | 0.6206 |
| net_win_rate | 0.4911 |
| gross_profit_factor | 1.0144 |
| gross_win_rate | 0.5021 |
| sharpe_ratio | -4.3961 |
| sortino_ratio | -1.6731 |
| max_drawdown | 0.8785 |
| cagr | -0.5532 |
| net_avg_win | 39.7662 |
| net_avg_loss | -61.8231 |
| avg_hold_time_bars | 9.1527 |
| exposure | 0.3025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
