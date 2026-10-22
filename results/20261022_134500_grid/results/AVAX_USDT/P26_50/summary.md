# EMA Hourly Continuation — AVAX/USDT P26_50

**Symbol:** AVAX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 898 |
| net_profit_factor | 0.4981 |
| net_win_rate | 0.4432 |
| gross_profit_factor | 0.9445 |
| gross_win_rate | 0.4543 |
| sharpe_ratio | -8.2404 |
| sortino_ratio | -3.4921 |
| max_drawdown | 0.9885 |
| cagr | -0.8266 |
| net_avg_win | 24.6325 |
| net_avg_loss | -39.3620 |
| avg_hold_time_bars | 3.4788 |
| exposure | 0.1420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
