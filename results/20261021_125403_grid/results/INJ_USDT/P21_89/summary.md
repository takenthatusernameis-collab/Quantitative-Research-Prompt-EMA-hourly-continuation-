# EMA Hourly Continuation — INJ/USDT P21_89

**Symbol:** INJ/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.8382 |
| net_win_rate | 0.5042 |
| gross_profit_factor | 1.0173 |
| gross_win_rate | 0.5042 |
| sharpe_ratio | -1.2319 |
| sortino_ratio | -0.3853 |
| max_drawdown | 0.3947 |
| cagr | -0.1643 |
| net_avg_win | 78.2808 |
| net_avg_loss | -94.9800 |
| avg_hold_time_bars | 14.9160 |
| exposure | 0.3227 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
