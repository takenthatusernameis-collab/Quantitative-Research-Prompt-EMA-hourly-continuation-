# EMA Hourly Continuation — TFUEL/USDT P8_26

**Symbol:** TFUEL/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1661 |
| net_profit_factor | 0.4442 |
| net_win_rate | 0.3980 |
| gross_profit_factor | 0.8698 |
| gross_win_rate | 0.4226 |
| sharpe_ratio | -13.1318 |
| sortino_ratio | -7.5736 |
| max_drawdown | 0.9999 |
| cagr | -0.9773 |
| net_avg_win | 12.0924 |
| net_avg_loss | -17.9924 |
| avg_hold_time_bars | 3.8928 |
| exposure | 0.2926 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
