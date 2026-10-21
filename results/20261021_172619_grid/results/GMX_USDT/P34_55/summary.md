# EMA Hourly Continuation — GMX/USDT P34_55

**Symbol:** GMX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.5549 |
| net_win_rate | 0.4554 |
| gross_profit_factor | 0.8115 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -3.5951 |
| sortino_ratio | -1.0469 |
| max_drawdown | 0.7050 |
| cagr | -0.3812 |
| net_avg_win | 46.2016 |
| net_avg_loss | -69.6316 |
| avg_hold_time_bars | 5.5060 |
| exposure | 0.1039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
