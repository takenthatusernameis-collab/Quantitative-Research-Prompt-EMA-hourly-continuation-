# EMA Hourly Continuation — RENDER/USDT P12_20

**Symbol:** RENDER/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1284 |
| net_profit_factor | 0.4201 |
| net_win_rate | 0.4237 |
| gross_profit_factor | 0.8836 |
| gross_win_rate | 0.4463 |
| sharpe_ratio | -12.6091 |
| sortino_ratio | -6.8771 |
| max_drawdown | 0.9996 |
| cagr | -0.9727 |
| net_avg_win | 13.3094 |
| net_avg_loss | -23.2922 |
| avg_hold_time_bars | 2.1301 |
| exposure | 0.1444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
