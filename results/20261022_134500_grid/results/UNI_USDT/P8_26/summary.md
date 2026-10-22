# EMA Hourly Continuation — UNI/USDT P8_26

**Symbol:** UNI/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1571 |
| net_profit_factor | 0.4520 |
| net_win_rate | 0.4278 |
| gross_profit_factor | 0.8846 |
| gross_win_rate | 0.4443 |
| sharpe_ratio | -10.9026 |
| sortino_ratio | -6.0838 |
| max_drawdown | 0.9995 |
| cagr | -0.9520 |
| net_avg_win | 12.2693 |
| net_avg_loss | -20.2893 |
| avg_hold_time_bars | 3.5029 |
| exposure | 0.2501 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
