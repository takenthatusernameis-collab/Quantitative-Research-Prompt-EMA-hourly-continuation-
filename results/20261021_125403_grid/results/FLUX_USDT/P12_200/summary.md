# EMA Hourly Continuation — FLUX/USDT P12_200

**Symbol:** FLUX/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.9181 |
| net_win_rate | 0.5201 |
| gross_profit_factor | 1.0767 |
| gross_win_rate | 0.5201 |
| sharpe_ratio | -0.3965 |
| sortino_ratio | -0.0985 |
| max_drawdown | 0.2193 |
| cagr | -0.0479 |
| net_avg_win | 83.9331 |
| net_avg_loss | -99.0896 |
| avg_hold_time_bars | 55.4228 |
| exposure | 0.7507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
