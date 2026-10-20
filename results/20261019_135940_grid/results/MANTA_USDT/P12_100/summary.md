# EMA Hourly Continuation — MANTA/USDT P12_100

**Symbol:** MANTA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 620 |
| net_profit_factor | 0.6993 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 1.0017 |
| gross_win_rate | 0.4823 |
| sharpe_ratio | -3.4425 |
| sortino_ratio | -1.2108 |
| max_drawdown | 0.7676 |
| cagr | -0.4358 |
| net_avg_win | 60.5257 |
| net_avg_loss | -77.5493 |
| avg_hold_time_bars | 22.1129 |
| exposure | 0.6232 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
