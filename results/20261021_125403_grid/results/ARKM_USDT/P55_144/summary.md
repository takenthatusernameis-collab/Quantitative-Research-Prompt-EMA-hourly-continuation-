# EMA Hourly Continuation — ARKM/USDT P55_144

**Symbol:** ARKM/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.8498 |
| net_win_rate | 0.5099 |
| gross_profit_factor | 1.0334 |
| gross_win_rate | 0.5099 |
| sharpe_ratio | -0.9011 |
| sortino_ratio | -0.2430 |
| max_drawdown | 0.2941 |
| cagr | -0.1076 |
| net_avg_win | 78.1402 |
| net_avg_loss | -95.6716 |
| avg_hold_time_bars | 13.9377 |
| exposure | 0.2236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
