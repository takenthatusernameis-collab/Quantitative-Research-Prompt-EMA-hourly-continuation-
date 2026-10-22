# EMA Hourly Continuation — ETHFI/USDT P8_20

**Symbol:** ETHFI/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1741 |
| net_profit_factor | 0.4663 |
| net_win_rate | 0.4227 |
| gross_profit_factor | 0.8543 |
| gross_win_rate | 0.4360 |
| sharpe_ratio | -11.5515 |
| sortino_ratio | -6.7794 |
| max_drawdown | 0.9998 |
| cagr | -0.9660 |
| net_avg_win | 11.8663 |
| net_avg_loss | -18.6384 |
| avg_hold_time_bars | 2.5991 |
| exposure | 0.2057 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
