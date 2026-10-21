# EMA Hourly Continuation — DEXE/USDT P26_55

**Symbol:** DEXE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.6545 |
| net_win_rate | 0.4748 |
| gross_profit_factor | 0.8934 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -2.5965 |
| sortino_ratio | -0.7566 |
| max_drawdown | 0.5851 |
| cagr | -0.2934 |
| net_avg_win | 55.6752 |
| net_avg_loss | -76.9115 |
| avg_hold_time_bars | 12.8969 |
| exposure | 0.2445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
