# EMA Hourly Continuation — FLUX/USDT P12_55

**Symbol:** FLUX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 647 |
| net_profit_factor | 0.8077 |
| net_win_rate | 0.5147 |
| gross_profit_factor | 1.0260 |
| gross_win_rate | 0.5147 |
| sharpe_ratio | -1.4684 |
| sortino_ratio | -0.5371 |
| max_drawdown | 0.5725 |
| cagr | -0.2208 |
| net_avg_win | 58.7263 |
| net_avg_loss | -77.1086 |
| avg_hold_time_bars | 11.0355 |
| exposure | 0.3245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
