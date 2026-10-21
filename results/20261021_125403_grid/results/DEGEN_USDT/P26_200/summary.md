# EMA Hourly Continuation — DEGEN/USDT P26_200

**Symbol:** DEGEN/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.9205 |
| net_win_rate | 0.5164 |
| gross_profit_factor | 1.0619 |
| gross_win_rate | 0.5164 |
| sharpe_ratio | -0.4343 |
| sortino_ratio | -0.1088 |
| max_drawdown | 0.2066 |
| cagr | -0.0527 |
| net_avg_win | 93.6935 |
| net_avg_loss | -108.7050 |
| avg_hold_time_bars | 39.1579 |
| exposure | 0.5420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
