# EMA Hourly Continuation — VR/USDT P8_34

**Symbol:** VR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1284 |
| net_profit_factor | 0.4625 |
| net_win_rate | 0.3855 |
| gross_profit_factor | 0.7451 |
| gross_win_rate | 0.4019 |
| sharpe_ratio | -12.0171 |
| sortino_ratio | -5.9481 |
| max_drawdown | 0.9998 |
| cagr | -0.9635 |
| net_avg_win | 17.3773 |
| net_avg_loss | -23.5732 |
| avg_hold_time_bars | 6.9050 |
| exposure | 0.4030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
