# EMA Hourly Continuation — QI/USDT P8_89

**Symbol:** QI/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.6830 |
| net_win_rate | 0.4741 |
| gross_profit_factor | 0.9774 |
| gross_win_rate | 0.4802 |
| sharpe_ratio | -3.6349 |
| sortino_ratio | -1.3095 |
| max_drawdown | 0.8115 |
| cagr | -0.4625 |
| net_avg_win | 54.8022 |
| net_avg_loss | -72.3340 |
| avg_hold_time_bars | 21.0412 |
| exposure | 0.6246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
