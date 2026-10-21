# EMA Hourly Continuation — MNT/USDT P26_200

**Symbol:** MNT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 230 |
| net_profit_factor | 1.0036 |
| net_win_rate | 0.5478 |
| gross_profit_factor | 1.2116 |
| gross_win_rate | 0.5478 |
| sharpe_ratio | 0.0642 |
| sortino_ratio | 0.0141 |
| max_drawdown | 0.1358 |
| cagr | 0.0016 |
| net_avg_win | 87.3445 |
| net_avg_loss | -105.4421 |
| avg_hold_time_bars | 59.6696 |
| exposure | 0.6238 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
