# EMA Hourly Continuation — ORDI/USDT P12_34

**Symbol:** ORDI/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 601 |
| net_profit_factor | 0.7503 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9532 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -2.4337 |
| sortino_ratio | -0.8522 |
| max_drawdown | 0.6399 |
| cagr | -0.3241 |
| net_avg_win | 64.8474 |
| net_avg_loss | -80.5978 |
| avg_hold_time_bars | 6.7421 |
| exposure | 0.1842 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
