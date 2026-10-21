# EMA Hourly Continuation — DIA/USDT P20_144

**Symbol:** DIA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.7797 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 0.9587 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -1.5300 |
| sortino_ratio | -0.4465 |
| max_drawdown | 0.4881 |
| cagr | -0.1873 |
| net_avg_win | 69.6583 |
| net_avg_loss | -87.2304 |
| avg_hold_time_bars | 27.5943 |
| exposure | 0.5232 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
