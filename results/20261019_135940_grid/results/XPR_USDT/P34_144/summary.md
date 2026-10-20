# EMA Hourly Continuation — XPR/USDT P34_144

**Symbol:** XPR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.4560 |
| net_win_rate | 0.4408 |
| gross_profit_factor | 0.7474 |
| gross_win_rate | 0.4463 |
| sharpe_ratio | -5.1981 |
| sortino_ratio | -1.6971 |
| max_drawdown | 0.8802 |
| cagr | -0.5687 |
| net_avg_win | 30.4476 |
| net_avg_loss | -52.6329 |
| avg_hold_time_bars | 12.7559 |
| exposure | 0.3183 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
