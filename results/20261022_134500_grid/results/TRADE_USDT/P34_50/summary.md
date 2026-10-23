# EMA Hourly Continuation — TRADE/USDT P34_50

**Symbol:** TRADE/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.3593 |
| net_win_rate | 0.3822 |
| gross_profit_factor | 0.6789 |
| gross_win_rate | 0.3907 |
| sharpe_ratio | -8.7973 |
| sortino_ratio | -3.3225 |
| max_drawdown | 0.9866 |
| cagr | -0.8186 |
| net_avg_win | 20.4062 |
| net_avg_loss | -35.1430 |
| avg_hold_time_bars | 3.9817 |
| exposure | 0.1283 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
