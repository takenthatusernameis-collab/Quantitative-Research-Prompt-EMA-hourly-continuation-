# EMA Hourly Continuation — RUNE/USDT P20_200

**Symbol:** RUNE/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.6846 |
| net_win_rate | 0.4850 |
| gross_profit_factor | 0.9975 |
| gross_win_rate | 0.5050 |
| sharpe_ratio | -1.9732 |
| sortino_ratio | -0.4783 |
| max_drawdown | 0.4599 |
| cagr | -0.2076 |
| net_avg_win | 65.8019 |
| net_avg_loss | -90.5318 |
| avg_hold_time_bars | 51.1163 |
| exposure | 0.6994 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
