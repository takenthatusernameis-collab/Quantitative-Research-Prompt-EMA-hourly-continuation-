# EMA Hourly Continuation — FLUX/USDT P20_200

**Symbol:** FLUX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 405 |
| net_profit_factor | 0.6890 |
| net_win_rate | 0.4914 |
| gross_profit_factor | 0.9991 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -2.4740 |
| sortino_ratio | -0.6946 |
| max_drawdown | 0.5874 |
| cagr | -0.2875 |
| net_avg_win | 63.7951 |
| net_avg_loss | -89.4482 |
| avg_hold_time_bars | 34.7185 |
| exposure | 0.6391 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
