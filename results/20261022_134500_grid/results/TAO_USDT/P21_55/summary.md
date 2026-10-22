# EMA Hourly Continuation — TAO/USDT P21_55

**Symbol:** TAO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 976 |
| net_profit_factor | 0.6048 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.9464 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -5.5402 |
| sortino_ratio | -2.4240 |
| max_drawdown | 0.9483 |
| cagr | -0.6926 |
| net_avg_win | 31.2709 |
| net_avg_loss | -46.8604 |
| avg_hold_time_bars | 4.8709 |
| exposure | 0.2161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
