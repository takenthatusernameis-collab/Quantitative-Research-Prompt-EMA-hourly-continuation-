# EMA Hourly Continuation — ORDI/USDT P20_89

**Symbol:** ORDI/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.7031 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 0.8586 |
| gross_win_rate | 0.4607 |
| sharpe_ratio | -2.5195 |
| sortino_ratio | -0.7875 |
| max_drawdown | 0.6159 |
| cagr | -0.3037 |
| net_avg_win | 63.4079 |
| net_avg_loss | -77.0532 |
| avg_hold_time_bars | 16.0682 |
| exposure | 0.3535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
