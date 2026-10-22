# EMA Hourly Continuation — DCR/USDT P12_21

**Symbol:** DCR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1485 |
| net_profit_factor | 0.2899 |
| net_win_rate | 0.3919 |
| gross_profit_factor | 0.7130 |
| gross_win_rate | 0.4269 |
| sharpe_ratio | -13.5474 |
| sortino_ratio | -7.4247 |
| max_drawdown | 0.9999 |
| cagr | -0.9787 |
| net_avg_win | 7.0141 |
| net_avg_loss | -15.5942 |
| avg_hold_time_bars | 2.8155 |
| exposure | 0.1892 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
