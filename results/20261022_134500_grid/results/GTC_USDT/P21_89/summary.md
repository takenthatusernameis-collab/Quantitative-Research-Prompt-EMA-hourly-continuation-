# EMA Hourly Continuation — GTC/USDT P21_89

**Symbol:** GTC/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 691 |
| net_profit_factor | 0.6062 |
| net_win_rate | 0.4645 |
| gross_profit_factor | 0.9026 |
| gross_win_rate | 0.4776 |
| sharpe_ratio | -4.0060 |
| sortino_ratio | -1.4829 |
| max_drawdown | 0.8406 |
| cagr | -0.5064 |
| net_avg_win | 39.8068 |
| net_avg_loss | -56.9736 |
| avg_hold_time_bars | 11.7887 |
| exposure | 0.3703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
