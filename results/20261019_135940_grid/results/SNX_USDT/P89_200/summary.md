# EMA Hourly Continuation — SNX/USDT P89_200

**Symbol:** SNX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.6304 |
| net_win_rate | 0.4663 |
| gross_profit_factor | 0.9562 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -2.9493 |
| sortino_ratio | -0.8214 |
| max_drawdown | 0.6318 |
| cagr | -0.3190 |
| net_avg_win | 58.7921 |
| net_avg_loss | -81.4965 |
| avg_hold_time_bars | 11.1839 |
| exposure | 0.1953 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
