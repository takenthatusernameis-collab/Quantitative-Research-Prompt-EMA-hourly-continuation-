# EMA Hourly Continuation — XEC/USDT P8_26

**Symbol:** XEC/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1555 |
| net_profit_factor | 0.4780 |
| net_win_rate | 0.4244 |
| gross_profit_factor | 1.0161 |
| gross_win_rate | 0.4521 |
| sharpe_ratio | -11.8456 |
| sortino_ratio | -6.5834 |
| max_drawdown | 0.9998 |
| cagr | -0.9638 |
| net_avg_win | 13.8686 |
| net_avg_loss | -21.3978 |
| avg_hold_time_bars | 4.3492 |
| exposure | 0.3060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
