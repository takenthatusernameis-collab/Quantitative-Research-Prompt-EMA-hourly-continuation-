# EMA Hourly Continuation — VR/USDT P34_89

**Symbol:** VR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.6189 |
| net_win_rate | 0.4465 |
| gross_profit_factor | 0.8034 |
| gross_win_rate | 0.4465 |
| sharpe_ratio | -2.7496 |
| sortino_ratio | -0.7037 |
| max_drawdown | 0.5637 |
| cagr | -0.2787 |
| net_avg_win | 62.2795 |
| net_avg_loss | -81.1652 |
| avg_hold_time_bars | 13.6820 |
| exposure | 0.2034 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
