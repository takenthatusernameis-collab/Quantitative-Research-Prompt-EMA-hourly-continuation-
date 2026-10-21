# EMA Hourly Continuation — TAO/USDT P12_55

**Symbol:** TAO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 599 |
| net_profit_factor | 0.8343 |
| net_win_rate | 0.4975 |
| gross_profit_factor | 1.0105 |
| gross_win_rate | 0.4975 |
| sharpe_ratio | -1.5891 |
| sortino_ratio | -0.5566 |
| max_drawdown | 0.5247 |
| cagr | -0.2282 |
| net_avg_win | 80.7899 |
| net_avg_loss | -95.8713 |
| avg_hold_time_bars | 11.3823 |
| exposure | 0.3099 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
