# EMA Hourly Continuation — SWFTC/USDT P26_55

**Symbol:** SWFTC/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 891 |
| net_profit_factor | 0.3328 |
| net_win_rate | 0.3906 |
| gross_profit_factor | 0.6349 |
| gross_win_rate | 0.4007 |
| sharpe_ratio | -9.5100 |
| sortino_ratio | -4.0171 |
| max_drawdown | 0.9941 |
| cagr | -0.8700 |
| net_avg_win | 14.2451 |
| net_avg_loss | -27.4359 |
| avg_hold_time_bars | 4.4725 |
| exposure | 0.1811 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
