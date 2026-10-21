# EMA Hourly Continuation — POKT/USDT P12_89

**Symbol:** POKT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 553 |
| net_profit_factor | 0.6271 |
| net_win_rate | 0.4087 |
| gross_profit_factor | 0.7723 |
| gross_win_rate | 0.4087 |
| sharpe_ratio | -4.2027 |
| sortino_ratio | -1.3879 |
| max_drawdown | 0.8086 |
| cagr | -0.4746 |
| net_avg_win | 59.7263 |
| net_avg_loss | -65.8293 |
| avg_hold_time_bars | 20.8228 |
| exposure | 0.5211 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
