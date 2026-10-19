# EMA Hourly Continuation — SEI/USDT P21_50

**Symbol:** SEI/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 952 |
| net_profit_factor | 0.5429 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.9194 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -6.6853 |
| sortino_ratio | -2.9018 |
| max_drawdown | 0.9730 |
| cagr | -0.7575 |
| net_avg_win | 26.2195 |
| net_avg_loss | -41.5072 |
| avg_hold_time_bars | 4.7006 |
| exposure | 0.2034 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
