# EMA Hourly Continuation — CVX/USDT P34_144

**Symbol:** CVX/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.6075 |
| net_win_rate | 0.4533 |
| gross_profit_factor | 0.8548 |
| gross_win_rate | 0.4634 |
| sharpe_ratio | -3.4337 |
| sortino_ratio | -1.0741 |
| max_drawdown | 0.7202 |
| cagr | -0.3978 |
| net_avg_win | 49.9814 |
| net_avg_loss | -68.2086 |
| avg_hold_time_bars | 17.2886 |
| exposure | 0.3866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
