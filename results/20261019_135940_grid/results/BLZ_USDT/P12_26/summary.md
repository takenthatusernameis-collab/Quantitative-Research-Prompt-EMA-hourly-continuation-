# EMA Hourly Continuation — BLZ/USDT P12_26

**Symbol:** BLZ/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1384 |
| net_profit_factor | 0.3752 |
| net_win_rate | 0.3858 |
| gross_profit_factor | 0.8240 |
| gross_win_rate | 0.4097 |
| sharpe_ratio | -12.4216 |
| sortino_ratio | -6.5201 |
| max_drawdown | 0.9997 |
| cagr | -0.9625 |
| net_avg_win | 11.2443 |
| net_avg_loss | -18.8258 |
| avg_hold_time_bars | 3.8439 |
| exposure | 0.2408 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
