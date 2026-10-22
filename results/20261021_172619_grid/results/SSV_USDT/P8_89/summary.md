# EMA Hourly Continuation — SSV/USDT P8_89

**Symbol:** SSV/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.7324 |
| net_win_rate | 0.4588 |
| gross_profit_factor | 0.8714 |
| gross_win_rate | 0.4609 |
| sharpe_ratio | -2.3166 |
| sortino_ratio | -0.7128 |
| max_drawdown | 0.6162 |
| cagr | -0.2801 |
| net_avg_win | 71.0691 |
| net_avg_loss | -82.2543 |
| avg_hold_time_bars | 31.5793 |
| exposure | 0.6759 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
