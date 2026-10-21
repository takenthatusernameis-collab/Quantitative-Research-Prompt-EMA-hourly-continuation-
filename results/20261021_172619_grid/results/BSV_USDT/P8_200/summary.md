# EMA Hourly Continuation — BSV/USDT P8_200

**Symbol:** BSV/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.6732 |
| net_win_rate | 0.4554 |
| gross_profit_factor | 0.8277 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -2.2406 |
| sortino_ratio | -0.5814 |
| max_drawdown | 0.4949 |
| cagr | -0.2349 |
| net_avg_win | 65.8940 |
| net_avg_loss | -81.8369 |
| avg_hold_time_bars | 51.3065 |
| exposure | 0.7836 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
