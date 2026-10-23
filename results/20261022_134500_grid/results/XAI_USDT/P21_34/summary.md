# EMA Hourly Continuation — XAI/USDT P21_34

**Symbol:** XAI/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1239 |
| net_profit_factor | 0.4686 |
| net_win_rate | 0.3947 |
| gross_profit_factor | 0.8484 |
| gross_win_rate | 0.4221 |
| sharpe_ratio | -11.0600 |
| sortino_ratio | -5.5291 |
| max_drawdown | 0.9990 |
| cagr | -0.9357 |
| net_avg_win | 18.0130 |
| net_avg_loss | -25.0643 |
| avg_hold_time_bars | 2.7958 |
| exposure | 0.1575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
