# EMA Hourly Continuation — ARKM/USDT P20_26

**Symbol:** ARKM/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 199 |
| net_profit_factor | 0.7495 |
| net_win_rate | 0.5075 |
| gross_profit_factor | 1.0270 |
| gross_win_rate | 0.5075 |
| sharpe_ratio | -1.2819 |
| sortino_ratio | -0.2600 |
| max_drawdown | 0.3164 |
| cagr | -0.1122 |
| net_avg_win | 76.5040 |
| net_avg_loss | -105.2021 |
| avg_hold_time_bars | 4.1156 |
| exposure | 0.0372 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
