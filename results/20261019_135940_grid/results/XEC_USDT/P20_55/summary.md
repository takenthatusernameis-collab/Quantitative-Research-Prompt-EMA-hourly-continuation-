# EMA Hourly Continuation — XEC/USDT P20_55

**Symbol:** XEC/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1016 |
| net_profit_factor | 0.4787 |
| net_win_rate | 0.4469 |
| gross_profit_factor | 0.9270 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -7.8014 |
| sortino_ratio | -3.5089 |
| max_drawdown | 0.9871 |
| cagr | -0.8209 |
| net_avg_win | 19.9626 |
| net_avg_loss | -33.6876 |
| avg_hold_time_bars | 5.9419 |
| exposure | 0.2732 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
