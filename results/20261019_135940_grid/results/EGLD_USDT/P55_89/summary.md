# EMA Hourly Continuation — EGLD/USDT P55_89

**Symbol:** EGLD/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.4058 |
| net_win_rate | 0.4642 |
| gross_profit_factor | 0.8211 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -5.8834 |
| sortino_ratio | -2.1278 |
| max_drawdown | 0.9307 |
| cagr | -0.6507 |
| net_avg_win | 20.7960 |
| net_avg_loss | -44.4038 |
| avg_hold_time_bars | 4.1202 |
| exposure | 0.1230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
